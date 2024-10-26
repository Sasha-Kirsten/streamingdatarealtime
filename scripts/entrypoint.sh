#!/bin/bash
set -e


# Install requirements if the requirements.txt file exists
if [  -e "/Users/aleksanderkirsten/streamingdatarealtime/requirements.txt"  ]; then
    # $(command python) pip install --upgrade pip
    # python -m pip install --upgrade pip
    $(command -v pip) install --user -r /Users/aleksanderkirsten/streamingdatarealtime/requirements.txt
    # pip install --user -r /Users/aleksanderkirsten/streamingdatarealtime/requirements.txt
fi


# Initialize the Airflow database and create an admin user if the database does not exist
if [  ! -f "/Users/aleksanderkirsten/streamingdatarealtime/airflow.db"  ]; then
    airflow db init  && \
    airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password admin
fi

# Upgrade the database schema
$(command -v airflow) db upgrade 

# Start the Airflow webserver
exec airflow webserver

