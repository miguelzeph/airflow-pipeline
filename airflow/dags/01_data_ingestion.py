from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
    ],
)

# Constants
base_url = "https://jsonplaceholder.typicode.com/todos/{id}"

# Function to extract data from the API
def extract_data(**kwargs):
    """
    This function extracts data from the JSONPlaceholder API.
    Returns a list of JSON objects.
    """
    list_obj = [requests.get(base_url.format(id=id)).json() for id in range(1, 11)]
    return list_obj

# Function to validate the extracted data
def validate_data(ti, **kwargs):
    """
    Validates each JSON object. If the data is valid, the function prints "Object okay".
    """
    list_obj = ti.xcom_pull(task_ids='extract_data')
    
    validated_obj = []
    for obj in list_obj:
        if obj:
            validated_obj.append(obj)
            
    return validated_obj

# Function to simulate saving data to a database
def save_database(ti, **kwargs):
    """
    Simulates saving the validated data to a database.
    """
    list_obj_validated = ti.xcom_pull(task_ids='validate_data')
    logging.info("SAVING data to the database...")
    for obj in list_obj_validated:
        logging.info(f"Saved object {obj['id']} was saved...")

# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    dag_id='data_ingestion_and_validation_dag',
    default_args=default_args,
    description='DAG to extract, validate, and save data from an API',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['data-ingestion', 'validation', 'save'],
) as dag:

    # Task to extract data from the API
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    # Task to validate the extracted data
    validate_task = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data,
        provide_context=True,
    )

    # Task to save the validated data
    save_task = PythonOperator(
        task_id='save_database',
        python_callable=save_database,
        provide_context=True,
    )

    # Define the order of tasks in the DAG
    extract_task >> validate_task >> save_task
