# from datetime import datetime, timedelta

# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.decorators import task, dag


# default_args = {
#     'owner': 'kvktran',
#     'retries': 5,
#     'retry_delay': timedelta(minutes=5)
# }

# @dag(
#     default_args=default_args,
#     dag_id='task_flow_api',
#     description='Our first dag using task flow api',
#     start_date=datetime(2024, 10, 8),
#     schedule_interval=timedelta(days=1)
# )
# def task_flow_api():

#     @task(multiple_outputs=True)
#     def get_name():
#         return {
#             "first_name": 'Donald',
#             "last_name": 'Tran'
#         }

#     @task
#     def get_age():
#         return 25

#     @task
#     def greet(first_name, last_name, age):
#         print(f"Hello World!!!, This is {first_name} {last_name} with {age} years old!")

#     name = get_name()
#     age = get_age()
#     greet(name["first_name"], name["last_name"], age)


# my_dag = task_flow_api()