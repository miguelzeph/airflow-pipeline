# Airflow Pipeline

## Setting Up Apache airflow Environment
In order to set up and manage your Apache Airflow project effectively, you will need to create a virtual environment and install the necessary dependencies. This guide will walk you through the process using Virtualenv. If you prefer to use a different virtual environment manager such as Anaconda, feel free to adapt the steps accordingly.

#### Install Virtualenv
```python
pip install virtualenv
```
#### Create a Virtual Environment
Start a new env and also select the python version (python version have to be installed in your machine)
```python
virtualenv --python=python3.7 env
```

Access the env
```python
source env/bin/activate
```

#### Install the dependencies
```
pip install -r requirements.txt
```

#### Define the AIRFLOW_HOME
You need to specify a home folder for Apache Airflow. Execute the following command to define it:

```bash
export AIRFLOW_HOME=$(pwd)/src/airflow
```

Your project structure should look like this:
```bash
project
│
├── env
│
└── src
    │
    └── airflow # airflow will create this folder
        │
        └── dags # All you have to do is populate this folder with your DAGs
```
### Initialize the Airflow Database

```bash
airflow db init
```

### Create an Admin User
Create an admin user for Airflow. Replace `admin`, `test@gmail.com`, and `admin` with your desired username, email, and password:

```bash
airflow users create -u admin -p admin -r Admin -f admin -l admin -e test@gmail.com
```

### Start the `Webserver` and `Scheduler` 
P.S - Don't forget to set up the `AIRFLOW_HOME` as mentioned before.

Open a terminal and run the following command to start the Airflow webserver on port 8080:
```bash
airflow webserver -p 8080
```

Open another terminal and make sure to export the AIRFLOW_HOME variable again. Start the Airflow Scheduler:
```bash
airflow scheduler
```
You can run both the webserver , scheduler and others dependecies using the following command (**Airflow Standalone is for development purposes only. Do not use this in production!**):

```bash
airflow standalone
```

### Important: Modifying Environment Variables (airflow.cfg)
When you need to modify settings within the `airflow.cfg` file, you can do it directly on the file when you want to run it locally or do some test.
```bash
project
│
├── env
│
└── src
    │
    └── airflow
        │
        └── airflow.cfg # Modify here       
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

### Environment Variable for this project
If you don't want to care with the environment variable, we provided a .env file for this project:
```bash
souce .env
```

## Authors

- Miguel Angelo do Amaral Junior: Data Engineer