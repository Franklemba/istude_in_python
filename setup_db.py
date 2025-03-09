import pymysql
from utils.db_utils import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def setup_database():
    # Connect to MySQL server
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    
    try:
        with connection.cursor() as cursor:
            # Create database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"Database '{DB_NAME}' created or already exists.")
            
            # Select the database
            cursor.execute(f"USE {DB_NAME}")
            
        connection.commit()
        print("Database setup completed successfully.")
        
    except Exception as e:
        print(f"Error setting up database: {e}")
    
    finally:
        connection.close()

if __name__ == "__main__":
    setup_database()