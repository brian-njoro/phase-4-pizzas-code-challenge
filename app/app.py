from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS  # Import Flask-CORS
from routes import create_app
from models.pizza import db  # Import your SQLAlchemy instance

app = create_app()

# Configure CORS - allow all origins by default
CORS(app)

# Configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

