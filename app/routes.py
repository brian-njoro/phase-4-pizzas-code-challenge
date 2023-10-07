from flask import Flask, current_app, make_response, request, jsonify, g
from flask_cors import CORS
import os
from models.restaurantpizza import restaurant_pizza
from models.restaurant import Restaurant
from models.pizza import Pizza,db

def create_app():
    app = Flask(__name__)
    
    # Allow CORS for all routes
    CORS(app)
    app.config.from_object('config.Config')
    db.init_app(app)

    @app.before_request
    def app_path():
        g.path = os.path.abspath(os.getcwd())

    @app.route('/Home')
    def home():
        return '<h2>Flask app for Restaurants</h2>'

    @app.route('/restaurants')
    def get_restaurants():
        restaurants = Restaurant.query.all()
        restaurant_list = []
        for restaurant in restaurants:
            restaurant_info = {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            }
            restaurant_list.append(restaurant_info)
        return jsonify(restaurant_list)
 
    @app.route('/restaurants/<int:id>')
    def get_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if restaurant is None:
            return jsonify({'error': 'Restaurant not found'}), 404
        
        restaurant_info = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': []
        }
        for pizza in restaurant.pizzas:
            pizza_info = {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            }
            restaurant_info['pizzas'].append(pizza_info)
        return jsonify(restaurant_info)
    
    @app.route('/pizzas')
    def get_pizzas():
        try:
            pizzas = Pizza.query.all()
            pizza_data = [pizza.serialize() for pizza in pizzas]
            return jsonify(pizza_data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/restaurant/<int:id>', methods=['DELETE'])
    def delete_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if restaurant is None:
            return jsonify({'error': 'Restaurant not found'}), 404
        
        # Deleting RestaurantPizza entries
        restaurant_pizza.query.filter_by(restaurant_id=id).delete()

        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    
    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        data = request.json
        if not all(key in data for key in ['price', 'pizza_id', 'restaurant_id']):
            return jsonify({'errors': ['validation errors']}), 400
        
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']

        pizza = Pizza.query.get(pizza_id)
        if pizza is None:
            return jsonify({'error': 'Pizza not found'}), 404
        
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant is None:
            return jsonify({'error': 'Restaurant not found'}), 404

        restaurant_pizza = restaurant_pizza(price=data['price'], pizza=pizza, restaurant=restaurant )
        db.session.add(restaurant_pizza)
        db.session.commit()

        return jsonify({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }),201
    
    return app




