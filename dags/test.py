import psycopg2

# Database connection details
DB_HOST = "localhost"  # Assuming PostgreSQL is running on your local machine (Docker container bound to port 5432)
DB_PORT = "5555"       # PostgreSQL default port
DB_NAME = "airflow"   # Default PostgreSQL database
DB_USER = "airflow"   # Default PostgreSQL user
DB_PASSWORD = "airflow"  # The password you set for the container

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

    # Create a table if it doesn't already exist
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        position VARCHAR(100),
        salary NUMERIC
    );
    '''
    cursor.execute(create_table_query)
    connection.commit()

    # Insert data into the table
    insert_query = '''
    INSERT INTO employees (name, position, salary)
    VALUES (%s, %s, %s);
    '''
    employees = [
        ("John Doe", "Software Engineer", 70000),
        ("Jane Smith", "Data Scientist", 80000),
        ("Mike Johnson", "DevOps Engineer", 75000),
    ]

    # Execute multiple inserts in one go
    cursor.executemany(insert_query, employees)
    connection.commit()

    print(f"{cursor.rowcount} records inserted successfully into employees table")

except Exception as error:
    print(f"Error while inserting into PostgreSQL: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")