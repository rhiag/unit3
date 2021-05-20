"""Main app roouting file"""
from flask import Flask, render_template
from app.models import db, Movies
import requests

def create_app():
    """Creates and configures an instance of the flask application"""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route("/")
    def root():
        return "Welcome"

    @app.route('/get_movie/<movie_id>', methods=['GET'])
    def get_movie(movie_id):
        """
        1. Accept input movie id
        2. App sends get request to api with movie id
        3. collects response from api
        4. Save to Database in Movies table
        5. Return movie details from database
        """
        response = requests.get(f"https://yts.mx/api/v2/movie_details.json?movie_id={movie_id}").json()
        print(response)

        movie_id = response['data']['movie']['id']
        title = response['data']['movie']['title']
        imdb_code = response['data']['movie']['imdb_code']
        like_count = response['data']['movie']['like_count']

        insert_movies(movie_id,title,imdb_code,like_count)
        return f"Movie titled '{title}' added!"


    
    @app.route('/reset')
    def reset():
        db.drop_all()
        db.create_all()
        return render_template("base.html", title="Home", movies=Movies.query.all())


    return app


def insert_movies(movie_id, title, imdb_code, like_count):
        movie = Movies(movie_id=movie_id, title=title,imdb_code=imdb_code,like_count=like_count)
        db.session.add(movie)
        db.session.commit()