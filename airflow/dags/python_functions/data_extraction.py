from typing import Any
import requests
import logging

# Instance
logger = logging.getLogger(__name__)

# Constants
base_url = "https://jsonplaceholder.typicode.com/todos/{id}"

# Function to extract data from the API
def extract_data() -> list[dict[str, Any]]:
    """
    This function extracts data from the JSONPlaceholder API.
    Returns a list of JSON objects.
    Output:
    [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": false
        },...
    ]
    """
    
    list_obj = [requests.get(base_url.format(id=id)).json() for id in range(1, 11)]
    
    return list_obj
