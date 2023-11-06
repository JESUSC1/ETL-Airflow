from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'me',
    'start_date': datetime(2021, 8, 23),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def print_data():
    print('data')

with DAG('airflow_tutorial_v01',
         default_args=default_args,
         schedule_interval=timedelta(hours=1),
         catchup=False
         ) as dag:

    print_data = PythonOperator(task_id='print_data',
                                python_callable=print_data)
    
    sleep = BashOperator(task_id='sleep',
                         bash_command='sleep 5')
    
    print_pipeline = BashOperator(task_id='print_pipeline',
                                  bash_command='echo pipeline')


print_data >> sleep >> print_pipeline
