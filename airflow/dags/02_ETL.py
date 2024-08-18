from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from python_functions.data_extraction import extract_data
from python_functions.data_transform import transform_etl
from python_functions.data_load import load_data

# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    dag_id='02_ETL',
    default_args=default_args,
    description='DAG - Pipeline ETL',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['data-ingestion', 'etl'],
) as dag:

    # Task to extract data from the API
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    # Task to validate the extracted data
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_etl,
        op_kwargs={ # Passing parameters to python function
            'task_ids': 'extract_data'
        },
        provide_context=True,
    )

    # Task to save the validated data
    load_task = PythonOperator(
        task_id='load_data',
        op_kwargs={ # Passing parameters to python function
            'task_ids': 'transform_data'
        },
        python_callable=load_data,
        provide_context=True,
    )

    # Define the order of tasks in the DAG
    extract_task >> transform_task >> load_task
