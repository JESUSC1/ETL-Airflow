from datetime import datetime, timedelta
import requests
import json
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


default_args = {
    'owner': 'jesus',
    'depends_on_past': False,
    'start_date': datetime.now() - timedelta(minutes=5), # set the start date to 5 minutes ago
    'end_date': datetime.now() + timedelta(minutes=5), # set the end date to 5 minutes from now
    'catchup': True # enable catchup, which will schedule any missed runs since the start date
}

with DAG(
    'collect_user_ingredients',
    default_args=default_args,
    description='Collect user ingredients from API and store in S3',
    schedule_interval='*/5 * * * *', # run every 5 minutes using the cron-like format
) as dag:

    def collect_user_ingredients():
        """
        Retrieves user ingredient submissions from the User Ingredient API and stores them in a list.
        """
        response = requests.get('https://airflow-miniproject.onrender.com')
        data = response.json()
        user_submission = {
            'pantry_data': data.get('pantry', {}),
            'user_data': data.get('user', {}),
        }
        with open('/tmp/user_ingredients.json', 'w') as f:
            json.dump(user_submission, f)

    def write_user_ingredients_to_s3():
        """
        Uploads the collected user ingredient submissions to the specified S3 bucket.
        """
        s3_hook = S3Hook()
        s3_key = 'raw/user_ingredients.json'
        s3_hook.load_file(
            filename='/tmp/user_ingredients.json',
            key=s3_key,
            bucket_name='jesusc-airflow1',
            replace=True
        )

    collect_ingredients_task = PythonOperator(
        task_id='collect_user_ingredients_from_API',
        python_callable=collect_user_ingredients,
        dag=dag,
    )

    write_to_s3_task = PythonOperator(
        task_id='write_to_s3',
        python_callable=write_user_ingredients_to_s3,
        dag=dag,
    )

    collect_ingredients_task >> write_to_s3_task
