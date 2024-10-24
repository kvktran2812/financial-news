# This script is for delete all tables and data in PostgreSQL database

import psycopg2


# Database connection details
DB_HOST = "localhost"  # Assuming PostgreSQL is running on your local machine (Docker container bound to port 5432)
DB_PORT = "5555"       # PostgreSQL default port
DB_NAME = "airflow"   # Default PostgreSQL database
DB_USER = "airflow"   # Default PostgreSQL user
DB_PASSWORD = "airflow"  # The password you set for the container


def drop_table(table_name, cursor, connection):
    drop_table_query = f"DROP TABLE IF EXISTS {table_name};"
    cursor.execute(drop_table_query)
    connection.commit()

    print(f"Table {table_name} dropped successfully!")


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

    # Drop tables
    drop_table("stocks", cursor, connection)
    

except Exception as error:
    print(f"Error while clearing tables and data in PostgreSQL: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")