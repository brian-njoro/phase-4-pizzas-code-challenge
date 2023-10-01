from .dbconfig import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')


