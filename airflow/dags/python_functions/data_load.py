import os
import logging

# Instance
logger = logging.getLogger(__name__)


# Function to simulate saving data to a database
def save_database(task_ids: str, **kwargs):
    """
    Simulates saving the validated data to a database.
    """
    
    # Getting Parameters from Airflow Dags - Tasks
    ti = kwargs["ti"]
    
    list_obj_validated = ti.xcom_pull(task_ids=task_ids)
    logger.info("--------- SAVING data to the database ---------")
    for obj in list_obj_validated:
        logger.info(f"Saved object {obj['id']} was saved...")

# Define the loading function
def load_data(task_ids: str, **kwargs):
    # Retrieve the transformed data
    
    # Getting Parameters from Airflow Dags - Tasks
    ti = kwargs['ti']
    
    # Get a List of Ids
    list_of_ids = ti.xcom_pull(task_ids=task_ids)
    
    
    # Save the list of IDs to txt
    folder_path = './airflow/data_output/'
    file_name = "list_of_ids.txt"
    file_path = folder_path + file_name
    # Get the directory name from the file path
    directory = os.path.dirname(folder_path)

    # Check if the directory exists
    if not os.path.exists(directory):
        # Create the directory if it does not exist
        os.makedirs(directory)
        logger.info(f"Directory '{directory}' created")
    
    with open(file_path, 'w') as file:
        
        file.write("id\n")

        for id in list_of_ids:
            write = f"{id}\n"
            file.write(write)
    
    logger.info(f"Data successfully saved to {file_path}")