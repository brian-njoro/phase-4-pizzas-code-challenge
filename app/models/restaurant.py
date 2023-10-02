from .dbconfig import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    
    #one to many relationship with destination
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')


