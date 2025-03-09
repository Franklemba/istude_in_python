import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# Database configuration
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')

# Connection string

password = quote_plus(DB_PASSWORD)
DB_URI = f"mysql+pymysql://{DB_USER}:{password}@{DB_HOST}/{DB_NAME}"
# DB_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

print(f"Connecting to database: {DB_NAME} on {DB_HOST}")
