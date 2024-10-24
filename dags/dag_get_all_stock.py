from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task, dag

# import stockanalysis web scraping module
from stockanalysis.stock.overview import get_all_stocks

default_args = {
    'owner': 'kvktran',
    'retries': 10,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    default_args=default_args,
    dag_id='DAG_GET_ALL_STOCK',
    description='This DAG is used to get all stock general information',
    start_date=datetime.today(),
    schedule_interval=timedelta(days=1)
)
def dag_get_all_stocks():

    @task
    def get_stock_list():
        metadata, data = get_all_stocks()
        return metadata, data
    
    @task
    def transform_data(metadata, data):
        pass

    @task
    def load_data(metadata, data):
        pass

    metadata, data = get_stock_list()
    transform_data(metadata, data)
    load_data(metadata, data)



# Call the DAG function to run the DAG
get_stocks_dag = dag_get_all_stocks()