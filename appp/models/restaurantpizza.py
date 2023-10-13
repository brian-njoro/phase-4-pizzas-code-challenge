from .dbconfig import db
from sqlalchemy.orm import validates


restaurant_pizza = db.Table(
    'restaurant_pizza',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('price', db.Integer, nullable=False),
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id')),  
)

# @validates('price')
# def price_range(self, price):
#     if price < 1 or price > 30:
#         raise AssertionError('Price must be between 1 and 30')


@validates('price')
def validate_price(self, key, value):
    if not (1 <= value <= 30):
        raise ValueError("Price must be between 1 and 30")
    return value