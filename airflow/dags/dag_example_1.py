from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Default arguments to be used for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 14),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'dag_exampe_1',  # DAG ID
    default_args=default_args,
    description='A simple DAG to test Airflow',
    schedule_interval=timedelta(days=1),  # Run daily
)

# Python Functions

def print_hello():
    print("Hello, Airflow!")

def calculate_sum():
    result = 1 + 2
    print(f"The sum of 1 and 2 is {result}")

# Define tasks
start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

print_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

sum_task = PythonOperator(
    task_id='calculate_sum',
    python_callable=calculate_sum,
    dag=dag,
)

end_task = DummyOperator(
    task_id='end',
    dag=dag,
)

# Set up task dependencies
start_task >> print_task >> sum_task >> end_task
