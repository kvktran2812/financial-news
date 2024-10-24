from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from stockanalysis.stock.overview import get_stock_news_press_release


default_args = {
    'owner': 'kvktran',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}