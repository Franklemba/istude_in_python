import os
from dotenv import load_dotenv
from utils.db_utils import DB_URI

# Load environment variables
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'
    DEBUG = True
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False