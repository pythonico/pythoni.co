from datetime import date
import os

from flask import send_from_directory
from flask import Flask
from flask import render_template
from flask import request
from flask import current_app
from flask import redirect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pythonico:pythonico@localhost/pythonico'
db = SQLAlchemy(app)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(80))
    country = db.Column(db.String(80), unique=True)

    def __init__(self, name, location, country=""):
        self.name = name
        self.location = location
        self.country = country

    def __repr__(self):
        return '<User %r>' % self.username

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    currentlocation_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    bornlocation_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    borndate = db.Column(db.DateTime)
    birthdate = db.Column(db.String(80))
    blog = db.Column(db.String(120))

    def __init__(self, username, email, currentlocation_id, bornlocation_id, borndate, birthdate):
        self.username = username
        self.email = email
        self.currentlocation_id = currentlocation_id
        self.bornlocation_id = bornlocation_id
        self.borndate = borndate
        self.birthdate = birthdate

    def __repr__(self):
        return '<User %r>' % self.username


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(8000), unique=True)
    eventdate = db.Column(db.DateTime)
    location = db.Column(db.Integer, db.ForeignKey('place.id'))
    url = db.Column(db.String(80), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    address = db.Column(db.Integer, db.ForeignKey('place.id'))
    blog = db.Column(db.String(120))
    url = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username




@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template(
        "index.html",
        year=date.today().year,
    )

if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)
