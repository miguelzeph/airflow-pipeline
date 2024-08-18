from typing import Any
import logging

# Instance
logger = logging.getLogger(__name__)


# Function to validate the extracted data
def validate_data(task_ids: str, **kwargs) -> list[dict[str, Any]]:
    """
    Validates each JSON object. If the data is valid, the function prints "Object okay".
    """
    
    # Getting Parameters from Airflow Dags - Tasks
    ti = kwargs['ti']    
    
    logger.info("---------- Objects Validated -----------")
    list_obj = ti.xcom_pull(task_ids=task_ids)
    validated_obj = []
    for obj in list_obj:
        if obj: 
            logger.info(f"Obj validated:{obj}")
            validated_obj.append(obj)
            
    return validated_obj


def transform_etl(task_ids: str, **kwargs) -> list[str]:
    """Transforme obj in a list of ID"""
    
    # Getting Parameters from Airflow Dags - Tasks
    ti = kwargs['ti']
    
    list_obj = ti.xcom_pull(task_ids=task_ids)
    
    return [obj["id"] for obj in list_obj if obj.get("id")]
