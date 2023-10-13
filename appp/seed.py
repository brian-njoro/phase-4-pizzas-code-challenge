import random
from random import randint, choice as rc
from faker import Faker
from app import app
from models.restaurantpizza import restaurant_pizza
from models.restaurant import Restaurant
from models.pizza import Pizza,db


with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()
    db.session.commit()

  
    restaurants = [
        Restaurant(name="Pizza Pit", address="123 Main St"),
        Restaurant(name="Graceful Treats Pizzeria", address="456 Elm St"),
        Restaurant(name="Pizza Paradise", address="789 Oak St"),
        Restaurant(name="Slice of Heaven", address="101 Pine St"),
        Restaurant(name="The Pizza Hut", address="222 Maple St"),
        Restaurant(name="Pizza Planet", address="333 Birch St"),
        Restaurant(name="Pizzarella", address="444 Cedar St"),
        Restaurant(name="Pizza Central", address="555 Walnut St"),
        Restaurant(name="Crust & Crave", address="666 Spruce St"),
        Restaurant(name="Pizza Paradiso", address="777 Redwood St"),
        Restaurant(name="Pizza Junction", address="888 Pineapple St"),
        Restaurant(name="Cheesy Delight", address="999 Watermelon St"),
        Restaurant(name="Pizza World", address="1010 Strawberry St"),
        Restaurant(name="Saucy Slice", address="1111 Grape St"),
        Restaurant(name="Top Tomato Pizzeria", address="1212 Blueberry St"),
        Restaurant(name="Rustic Pies", address="1313 Raspberry St")
    ]

    
    pizzas = [
        Pizza(name="deluxe", ingredients="Tomato, Mozzarella, Basil"),
        Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni"),
        Pizza(name="Chicken Tikka", ingredients="Tomato, Mozzarella, Bell Peppers, Mushrooms"),
        Pizza(name="Hawaiian", ingredients="Tomato, Mozzarella, Ham, Pineapple"),
        Pizza(name="Supreme", ingredients="Tomato, Mozzarella, Pepperoni, Sausage, Bell Peppers, Onions, Olives"),
        Pizza(name="BBQ Chicken", ingredients="BBQ Sauce, Mozzarella, Chicken, Red Onion, Cilantro"),
        Pizza(name="Meat Lover's", ingredients="Tomato, Mozzarella, Pepperoni, Sausage, Bacon, Ground Beef"),
        Pizza(name="White Pizza", ingredients="Olive Oil, Mozzarella, Ricotta, Garlic, Spinach"),
        Pizza(name="Mushroom Delight", ingredients="Tomato, Mozzarella, Mushrooms, Garlic, Thyme"),
        Pizza(name="Buffalo Chicken", ingredients="Buffalo Sauce, Mozzarella, Chicken, Red Onion, Blue Cheese"),
        Pizza(name="Pesto Delight", ingredients="Pesto Sauce, Mozzarella, Cherry Tomatoes, Arugula"),
        Pizza(name="Four Cheese", ingredients="Tomato, Mozzarella, Parmesan, Gorgonzola, Ricotta"),
        Pizza(name="Veggie Supreme", ingredients="Tomato, Mozzarella, Bell Peppers, Onions, Mushrooms, Olives"),
        Pizza(name="Seafood Special", ingredients="Tomato, Mozzarella, Shrimp, Crab, Garlic, Parsley"),
        Pizza(name="Barbecue Beef", ingredients="BBQ Sauce, Mozzarella, Beef, Red Onion, Jalapeños"),
        Pizza(name="Spinach and Feta", ingredients="Tomato, Mozzarella, Spinach, Feta, Garlic")
    ]
    
    db.session.add_all(restaurants + pizzas)
    db.session.commit() 

    
    restaurant_pizza_info = []

    for _ in range(5):  
        for restaurant in restaurants:
            for pizza in pizzas:
                price = random.randint(1, 30)  
                association = {
                    "price": price,
                    "restaurant_id": restaurant.id,
                    "pizza_id": pizza.id
                }
                restaurant_pizza_info.append(association)

    
    db.session.execute(restaurant_pizza.insert().values(restaurant_pizza_info))
    db.session.commit()

    print("Successfully seeded data!!!!!")