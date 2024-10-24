from stockanalysis.stock.overview import *
from stockanalysis.transform.stock import *
import psycopg2

# Database connection details
DB_HOST = "localhost"  # Assuming PostgreSQL is running on your local machine (Docker container bound to port 5432)
DB_PORT = "5555"       # PostgreSQL default port
DB_NAME = "airflow"   # Default PostgreSQL database
DB_USER = "airflow"   # Default PostgreSQL user
DB_PASSWORD = "airflow"  # The password you set for the container


metadata, data = get_all_stocks()

for i in range(len(data)):
    value, unit = transform_market_cap(data[i][-1])
    data[i][-1] = value
    data[i].append(unit)


connection = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = connection.cursor()

query = """
INSERT INTO stocks (symbol, company_name, industry, market_cap, unit)
    VALUES (%s, %s, %s, %s, %s)
"""


cursor.executemany(query, data)
connection.commit()
connection.close()