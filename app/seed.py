from random import randint, choice as rc
from faker import Faker
from app import app
from models.restaurantpizza import restaurant_pizza
from models.restaurant import Restaurant
from models.pizza import Pizza,db
from datetime import datetime

fake = Faker()

def seed_data():
    with app.app_context():
        db.create_all()

        restaurant_pizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()

        restaurants = []
        for _ in range(40):
            name = fake.company()
            address = fake.address()
            r = Restaurant(name=name,address=address)
            restaurants.append(r)


        db.session.add_all(restaurants)
        db.session.commit()

        pizzas = []
        for _ in range(50):
            p = Pizza(name=fake.word(), price=randint(1, 30), created_at=datetime.now())
            pizzas.append(p)

        db.session.add_all(pizzas)
        db.session.commit()

        restaurant_pizzas = []
        for restaurant in restaurants:
            num_pizzas = randint(1, 5)
            sampled_pizzas = rc(pizzas, k=num_pizzas)
            for pizza in sampled_pizzas:
                rp = restaurant_pizza(restaurant_id=restaurant.id, pizza_id=pizza.id)
                restaurant_pizzas.append(rp)

        db.session.add_all(restaurant_pizzas)
        db.session.commit()

if __name__ == '__main__':
    seed_data()

