from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS  
from routes import create_app
from models.pizza import db  

app = create_app()

CORS(app)

# Configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

