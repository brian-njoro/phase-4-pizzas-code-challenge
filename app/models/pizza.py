from .dbconfig import db
from sqlalchemy.orm import validates
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    @validates('price')
    def validate_price(self, key, price):
        if not (1 <= price <= 30):
            raise ValueError('Price must be between 1 and 30.')
        return price
    
    pizza_restaurants = db.relationship('RestaurantPizza', back_populates='pizza')

