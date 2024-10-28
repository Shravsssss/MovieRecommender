from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import json
import sys
import csv
import time
import requests
from datetime import datetime
from streaming import search_movie_on_justwatch
from reviews import get_movie_reviews, search_movie_tmdb

sys.path.append("../../")
from Code.prediction_scripts.item_based import recommendForNewUser
from search import Search

import requests

app = Flask(__name__)
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_title = db.Column(db.String(200), nullable=False)
    recommended_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Recommendation {self.movie_title}>'

class Watchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(250), nullable=False)
    imdb_rating = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Replace 'YOUR_API_KEY' with your actual OMDB API key
OMDB_API_KEY = 'b726fa05'
api_key_TMDB = "9f385440fe752884a4f5b8ea5b6839dd"

def get_movie_info(title):
    index=len(title)-6
    url = f"http://www.omdbapi.com/?t={title[0:index]}&apikey={OMDB_API_KEY}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        platforms = search_movie_on_justwatch(title)
        movie_id = search_movie_tmdb(title, api_key_TMDB)
        reviews = get_movie_reviews(movie_id, api_key_TMDB)

        res=response.json()
        if(res['Response'] == "True"):
            return res
        else:  
            return { 'Title': title, 'Platforms': platforms, 'Reviews': reviews, 'imdbRating':"N/A", 'Genre':'N/A',"Poster":"https://www.creativefabrica.com/wp-content/uploads/2020/12/29/Line-Corrupted-File-Icon-Office-Graphics-7428407-1.jpg"}
    else:
        return  { 'Title': title, 'Platforms': platforms, 'Reviews': reviews, 'imdbRating':"N/A",'Genre':'N/A', "Poster":"https://www.creativefabrica.com/wp-content/uploads/2020/12/29/Line-Corrupted-File-Icon-Office-Graphics-7428407-1.jpg"}

@app.route("/")
def landing_page():
    if current_user.is_authenticated:
        return render_template("landing_page.html")
    else:
        return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('landing_page'))
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            error = 'Username is already taken. Please choose a different one.'
            return render_template('register.html', error=error)
        
        # If username is not taken, proceed with registration
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        # Automatically log in the user after registration
        login_user(user)

        # Redirect to the landing page after successful login
        return redirect(url_for('landing_page'))
    return render_template('register.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('landing_page'))

    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()  # 'user' is now defined here

        if user is None or not user.check_password(password):
            error = 'Invalid username or password'
        else:
            login_user(user)
            return redirect(url_for('landing_page'))

    # If we reach this point without returning, 'user' was not assigned due to a POST
    # Or there was an error in login, handle accordingly
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('landing_page'))



@app.route("/predict", methods=["POST"])
def predict():
    data = json.loads(request.data)  # contains movies
    data1 = data["movie_list"]
    training_data = []
    for movie in data1:
        movie_with_rating = {"title": movie, "rating": 5.0}
        training_data.append(movie_with_rating)
    recommendations = recommendForNewUser(training_data)
    recommendations = recommendations[:10]

    for movie in recommendations:
        movie_info = get_movie_info(movie)
        # print(movie_info['imdbRating'])
        if movie_info:
            # Comments
            movie_with_rating[movie+"-c"]=movie_info['Reviews']
            movie_with_rating[movie+"-s"]=movie_info['Platforms']
            movie_with_rating[movie+"-r"]=movie_info['imdbRating']
            movie_with_rating[movie+"-g"]=movie_info['Genre']
            movie_with_rating[movie+"-p"]=movie_info['Poster']
        
        new_recommendation = Recommendation(user_id=current_user.id, movie_title=movie)
        db.session.add(new_recommendation)
    
    db.session.commit()

    resp = {"recommendations": recommendations, "rating":movie_with_rating}
    return resp

@app.route("/history")
@login_required
def history():
    recommendations = Recommendation.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html', recommendations=recommendations)


@app.route("/search", methods=["POST"])
def search():
    term = request.form["q"]
    search = Search()
    filtered_dict = search.resultsTop10(term)
    resp = jsonify(filtered_dict)
    resp.status_code = 200
    return resp


@app.route('/watchlist')
@login_required
def view_watchlist():
    # Fetch the user's watchlist
    watchlist_movies = Watchlist.query.filter_by(user_id=current_user.id).all()
    
    # Check if the watchlist is empty
    if not watchlist_movies:
        flash("You have no movies in your watchlist.", "info")
        return render_template('watchlist.html', watchlist=watchlist_movies, empty=True)
    
    return render_template('watchlist.html', watchlist=watchlist_movies, empty=False)

@app.route('/add_to_watchlist', methods=['POST'])
@login_required
def add_to_watchlist():
    movie_title = request.form.get('movie_title')
    imdb_rating = request.form.get('imdb_rating')
    
    # Check if the movie is already in the user's watchlist
    existing_movie = Watchlist.query.filter_by(user_id=current_user.id, movie_title=movie_title).first()
    if existing_movie:
        flash('Movie is already in your watchlist!', 'warning')
        return redirect(url_for('view_watchlist'))
    
    # Add the movie to the user's watchlist
    new_movie = Watchlist(movie_title=movie_title, imdb_rating=imdb_rating, user_id=current_user.id)
    db.session.add(new_movie)
    db.session.commit()
    
    flash('Movie added to your watchlist!', 'success')
    return redirect(url_for('view_watchlist'))

@app.route('/remove_from_watchlist/<int:movie_id>', methods=['POST'])
@login_required
def remove_from_watchlist(movie_id):
    movie = Watchlist.query.get_or_404(movie_id)
    
    # Ensure the movie belongs to the current user
    if movie.user_id != current_user.id:
        flash('You do not have permission to remove this movie!', 'danger')
        return redirect(url_for('view_watchlist'))
    
    db.session.delete(movie)
    db.session.commit()
    
    flash('Movie removed from your watchlist.', 'success')
    return redirect(url_for('view_watchlist'))

@app.route("/feedback", methods=["POST"])
def feedback():
    data = json.loads(request.data)
    with open(f"experiment_results/feedback_{int(time.time())}.csv", "w") as f:
        for key in data.keys():
            f.write(f"{key} - {data[key]}\n")
    return data

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
