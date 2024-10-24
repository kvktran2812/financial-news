from datetime import datetime, timedelta
from airflow.decorators import task, dag
from airflow.hooks.base_hook import BaseHook

import psycopg2

# import stockanalysis web scraping module
from stockanalysis.stock.overview import get_all_stocks
from stockanalysis.transform.stock import transform_market_cap

default_args = {
    'owner': 'kvktran',
    'retries': 10,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    default_args=default_args,
    dag_id='dag_get_all_stocks',
    description='This DAG is used to get all stock general information',
    start_date=datetime.today(),
    schedule_interval=timedelta(days=1)
)
def dag_get_all_stocks():

    @task
    def get_stock_list():
        _, data = get_all_stocks()
        return data
    
    @task
    def transform_data(data):
        for i in range(len(data)):
            value, unit = transform_market_cap(data[i][-1])
            data[i][-1] = value
            data[i].append(unit)

        return data
        
        

    @task
    def load_data(data):
        stocks_insert_query = """
            INSERT INTO stocks (symbol, company_name, industry, market_cap, unit)
            VALUES (%s, %s, %s, %s, %s)
        """
        conn = BaseHook.get_connection('postgresql_conn')

        connection = psycopg2.connect(
            host=conn.host,
            port=conn.port,
            database=conn.schema,
            user=conn.login,
            password=conn.password
        )
        cursor = connection.cursor()
        cursor.executemany(stocks_insert_query, data)
        connection.commit()
        connection.close()

    data = get_stock_list()
    data = transform_data(data)
    load_data(data)
    

# Call the DAG function to run the DAG
get_stocks_dag = dag_get_all_stocks()