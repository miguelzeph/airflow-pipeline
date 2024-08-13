#!/bin/bash

export AIRFLOW_HOME=$(pwd)/src/airflow

echo "****** Starting DB*******"
airflow db init

sleep 5

echo "****** Creating User Admin*******"

airflow users create \
    --role Admin \
    --firstname admin \
    --lastname admin \
    --email admin_email@example.com \
    --username admin \
    --password admin

sleep 5

# Starting Airflow (standalone is only for production!)
echo "****** Starting Airflow*******"

# airflow standalone

airflow webserver -p 8080 &

sleep 5

airflow scheduler