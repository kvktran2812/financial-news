from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from stockanalysis.trending import get_trending


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    default_args=default_args,
    dag_id='get_trending_dag',
    description='Our first dag using python operator',
    start_date=datetime(2024, 10, 9),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=get_trending,
        # op_kwargs={'some_dict': {'a': 1, 'b': 2}}
    )