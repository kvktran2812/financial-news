from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task, dag
from airflow.providers.postgres.hooks.postgres import PostgresHook

# import stockanalysis web scraping module
from stockanalysis.stock.overview import get_all_stocks

import psycopg2

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
        metadata, data = get_all_stocks()
        return {
            "metadata": metadata,  
            "data": data
        }
    
    @task
    def transform_data(metadata, data):
        pass


    @task
    def create_table():
        hook = PostgresHook(postgres_conn_id='postgresql_conn')

        create_table_query = """
            CREATE TABLE IF NOT EXISTS stocks (
                id SERIAL PRIMARY KEY,
                symbol VARCHAR(8),
                company_name VARCHAR(128),
                industry VARCHAR(128),
                market_cap NUMERIC
            )
        """

        hook.run(create_table_query)
        print("Create table successfully!")
        

    @task
    def load_data(metadata, data):
        pass

    # t = get_stock_list()
    # metadata = t["metadata"]
    # data = t["data"]
    # metadata, data = None, None
    # transform_data(metadata, data)
    # load_data(metadata, data)

    create_table()



# Call the DAG function to run the DAG
get_stocks_dag = dag_get_all_stocks()