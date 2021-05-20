"""SQLAlchemy models and database architecture"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movies(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    imdb_code = db.Column(db.Unicode(10))
    title = db.Column(db.String(100), unique=True, nullable=False)
    like_count=db.Column(db.Integer,nullable=False)
    

    def __repr__(self):
        return '<Movies %r>' % self.title