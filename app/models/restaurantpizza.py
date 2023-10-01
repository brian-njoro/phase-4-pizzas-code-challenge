from .dbconfig import db
class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant = db.relationship('Restaurant', backref=db.backref('restaurant_pizza'))
    pizza = db.relationship('Pizza', backref=db.backref('restaurant_pizza'))

    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='pizza_restaurants')
