"""Example of a single file flask application that uses an open notify API"""
from datetime import datetime 
from flask import Flask , redirect
from flask_sqlalchemy import SQLAlchemy
import requests

#Create flask application instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Runs root when we navigate to / endpoint
@app.route('/')
def root():
    astro_data = Astro.query.all()
    return f'{astro_data}'

@app.route('/refresh')
def refresh():
    request = requests.get("http://api.open-notify.org/astros.json")
    response = request.json()
    num_of_astros = response["number"]
    record = Astro(num_astros = num_of_astros,time=datetime.now())
    db.session.add(record)
    db.session.commit()
    return redirect('/')

@app.route('/reset')
def reset():
    db.drop_all()
    db.create_all()
    return redirect('/refresh')


#Creating SQLAlchemy database
# Create Astro table
class Astro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_astros = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"# of Astros: {self.num_astros} at {self.time}"


