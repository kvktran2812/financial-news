# This script is for creating tables in PostgreSQL database

import psycopg2

# Database connection details
DB_HOST = "localhost"  # Assuming PostgreSQL is running on your local machine (Docker container bound to port 5432)
DB_PORT = "5555"       # PostgreSQL default port
DB_NAME = "airflow"   # Default PostgreSQL database
DB_USER = "airflow"   # Default PostgreSQL user
DB_PASSWORD = "airflow"  # The password you set for the container


def create_table(table_name, cursor, connection, query):
    cursor.execute(query)
    connection.commit()

    print(f"Table {table_name} created successfully!")
    

try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = connection.cursor()

    # Create tables queries setup
    create_stocks_table_query = '''
    CREATE TABLE IF NOT EXISTS stocks (
        id SERIAL PRIMARY KEY,
        symbol VARCHAR(8),
        company_name VARCHAR(128),
        industry VARCHAR(128),
        market_cap NUMERIC
    );
    '''

    # Create tables in PostgreSQL
    create_table("stocks", cursor, connection, create_stocks_table_query)

except Exception as error:
    print(f"Error while inserting into PostgreSQL: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")