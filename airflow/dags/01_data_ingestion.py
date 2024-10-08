from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from python_functions.data_extraction import extract_data
from python_functions.data_transform import validate_data
from python_functions.data_load import save_database

# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    dag_id='01_data_ingestion',
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
        op_kwargs={ # Passing parameters to python function
            'task_ids': 'extract_data'
        },
        provide_context=True,
    )

    # Task to save the validated data
    save_task = PythonOperator(
        task_id='save_database',
        op_kwargs={ # Passing parameters to python function
            'task_ids': 'validate_data'
        },
        python_callable=save_database,
        provide_context=True,
    )

    # Define the order of tasks in the DAG
    extract_task >> validate_task >> save_task
