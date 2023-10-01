from flask import Flask, request, jsonify, abort
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/Home')
def home():
    return '<h2>Flask app for Restaurants</h2>'