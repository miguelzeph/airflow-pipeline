# Airflow Pipeline

## Setting Up Apache airflow Environment
In order to set up and manage your Apache Airflow project effectively, you will need to create a virtual environment and install the necessary dependencies. This guide will walk you through the process using Virtualenv. If you prefer to use a different virtual environment manager such as Anaconda, feel free to adapt the steps accordingly.

## Preparing Python 3.11 Configuration

1. Install Virtualenv
```python
pip install virtualenv
```
2. Create a Virtual Environment
Start a new env and also select the python version (python version have to be installed in your machine)
```python
virtualenv --python=python3.11 env
```
3. Access the env
```python
source env/bin/activate
```
4. Install the dependencies
```
pip install -r requirements.txt
```

## Airfloe Main Components

- **DAGs:** Define the workflow and the sequence of tasks.
- **Tasks:** The units of work within a DAG.
- **Operators:** Define the logic of tasks. Examples include PythonOperator, BashOperator, and DummyOperator.
- **Scheduler:** Plans and executes tasks based on the DAG definitions.
- **Web Interface:** A graphical interface for monitoring and managing DAGs and tasks.
- **Executor:** Defines how tasks will be executed (e.g., LocalExecutor, CeleryExecutor, KubernetesExecutor).


## Configuring Airflow Locally (Optional)
**Note**: Before start If you're a Linux user, you can skip this entire section by simply executing the `entrypoint.sh` file, which will run all of these commands at once. However, for educational purposes, you can follow the instructions below to execute the program step by step.

```bash
bash entrypoint.sh
```

1. Define the enverinment variables
**IMPORTANT**: You need to specify specially the variable  **AIRFLOW_HOME** because is where Airflow stores its files (dags, logs, plugins, config). For this we have created an .env file with some basic env var.

```bash
source .env
```

2. Your project structure should look like this:
```bash
project
│
├── env
│
└── airflow # airflow will create this folder
        │
        └── dags # All you have to do is populate this folder with your DAGs
```
3. Initialize the Airflow Database

```bash
airflow db init
```

4. Create an Admin User
Create an admin user for Airflow. Replace `admin`, `test@gmail.com`, and `admin` with your desired username, email, and password:

```bash
airflow users create -u admin -p admin -r Admin -f admin -l admin -e test@gmail.com
```

5. Start the `Webserver` and `Scheduler` 
P.S - Don't forget to set up the `AIRFLOW_HOME` as mentioned before.

Open a terminal and run the following command to start the Airflow webserver on port 8080:
```bash
airflow webserver -p 8080
```

Open another terminal and make sure to export the AIRFLOW_HOME variable again. Start the Airflow Scheduler:
```bash
airflow scheduler
```
P.S. You can run both the webserver , scheduler and others dependecies using the following command (**Airflow Standalone is for development purposes only. Do not use this in production!**):

```bash
airflow standalone
```

## Modifying Environment Variables (airflow.cfg)
When you need to modify settings within the `airflow.cfg` file, you can do it directly on the file when you want to run it locally or do some test. I strongly recommend insert the variables in the file **.env** instead chage the airflow.cfg directly because the configuration won't be overwrited if you need to reset the airflow for some reason.

```bash
project
│
├── .env
│
└── airflow
    │
    └── airflow.cfg # <--- Modify here       
```

However, in production environment, is highly recommended always use the env vars. So In Apache Airflow, environment variables with **double underscores** `__` are specifically used to modify settings within the airflow.cfg configuration file. These variables are designed to provide granular control over the configuration options in the Airflow configuration file.

For example, if you have a configuration variable named my_variable within the airflow.cfg file, you can modify it by setting an environment variable in the format:

```bash
AIRFLOW__<SECTION_NAME>__<VARIABLE_NAME>=<NEW_VALUE>
```
Here: 
- <SECTION_NAME> refers to the section within the configuration file where the variable is located.
- <VARIABLE_NAME> is the name of the variable you want to modify.
- <NEW_VALUE> is the new value you want to assign to the variable.

For instance, if you want to change the load_examples variable within the core section of the airflow.cfg file to False, you would set the environment variable like this:

```bash
AIRFLOW__CORE__LOAD_EXAMPLES=False
```

Other example:

```bash
AIRFLOW__WEBSERVER__APP_THEME = "yeti.css"
```

## Core Project Structure
To test Airflow, you only need to focus on the Python files inside the dags folder.
```bash
.
├── airflow
│   ├── dags           # Directory to save your DAGs and Python code
│   │   └── dag_example_1.py  # Example DAG file
├── entrypoint.sh      # Script to automate the setup process for Airflow
├── .env               # Configuration file for environment variables
└── requirements.txt   # File listing Python libraries

```

## DAGs

### What is a DAG?
A **DAG (Directed Acyclic Graph)** is a fundamental concept in Apache Airflow that represents a series of tasks organized in a way that reflects their dependencies. The "Directed" part indicates that the workflow has a defined order, where one task leads to the next. "Acyclic" ensures that the workflow does not loop back on itself, preventing any circular dependencies.

In simpler terms, a DAG is a collection of all the tasks you want to run, organized in a way that clearly shows their relationships and order of execution.

### Example DAGs Ordered by Level of Complexity

Below is a list of example DAGs, ordered from the most basic to more advanced workflows. These examples cover a range of common data engineering tasks:

1. **Data Ingestion**  
   Ingesting data from various sources such as APIs, databases, or files into a data lake or data warehouse.

2. **ETL/ELT Pipelines**  
   Extracting, Transforming, and Loading (ETL) data, or Extracting, Loading, and Transforming (ELT) data into a target system, typically for further analysis.

3. **Updating Dimension and Fact Tables**  
   Maintaining and updating tables in a data warehouse, including both dimension tables (containing master data) and fact tables (containing transactional data).

4. **Data Quality Checks**  
   Verifying the accuracy, completeness, and reliability of data after it has been ingested or transformed.

5. **Data Aggregation and Summary Pipelines**  
   Aggregating large datasets into summaries or key metrics that can be used for reporting or analysis.

6. **Machine Learning Pipelines**  
   Orchestrating the end-to-end process of training, validating, and deploying machine learning models.

7. **Streaming Pipelines**  
   Processing and analyzing data in real-time or near real-time, often integrating with tools like Apache Kafka or Spark.

8. **Reports and Dashboards**  
   Automating the generation of reports and updating dashboards with the latest data.

9. **Monitoring and Alerts**  
   Continuously monitoring data pipelines and system health, with automated alerts triggered by specific conditions or failures.

10. **Data Archival and Deletion**  
    Managing the lifecycle of data by archiving or deleting old or obsolete data, ensuring compliance with data retention policies.

11. **Continuous Integration Pipelines (CI/CD)**  
    Automating the testing and deployment of data pipeline code, ensuring that new updates can be rolled out smoothly and efficiently.


## Authors

- Miguel Angelo do Amaral Junior: Data Engineer