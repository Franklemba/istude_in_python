from flask import Flask
from config import Config
from models.database import db
from routes import home_bp, about_bp, contact_bp
from dotenv import load_dotenv

# local database configuration
# import pymysql

# pymysql.install_as_MySQLdb()

load_dotenv()

def create_app(config_class=Config):
    # Initialize the Flask application
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    
    # Initialize database
    db.init_app(app)
    
    
    # Create database tables if the y din't exist
    with app.app_context():
        db.create_all()
        
    
    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    
    
    return app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

    
    
