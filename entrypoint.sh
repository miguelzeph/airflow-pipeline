#!/bin/bash

echo "****** Setting Up Environment Variables for Airflow *******"
# Enable automatic export of all variables defined after this point
set -a
# Load environment variables from .env file
source .env
# Disable automatic export of variables
set +a

echo "AIRFLOW_HOME=${AIRFLOW_HOME}"
echo "AIRFLOW_UID=${AIRFLOW_UID}"
echo "AIRFLOW__CORE__LOAD_EXAMPLE=${AIRFLOW__CORE__LOAD_EXAMPLES}"
echo "AIRFLOW__WEBSERVER__HOST=${AIRFLOW__WEBSERVER__HOST}"
echo "AIRFLOW__WEBSERVER__PORT=${AIRFLOW__WEBSERVER__PORT}"

echo "****** Starting DB *******"
airflow db init

sleep 5

echo "****** Creating User Admin *******"
airflow users create \
    --role Admin \
    --firstname admin \
    --lastname admin \
    --email admin_email@example.com \
    --username admin \
    --password admin

sleep 5

echo "****** Starting Airflow *******"
airflow webserver -p 8080 &
airflow scheduler
