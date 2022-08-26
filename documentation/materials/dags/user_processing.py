
from airflow import DAG
from datetime import datetime

from airflow.providers.postgres.operators.postgres import PostgresOperator

# catchup parameters, default means that the dag will run anlyway even, otherwise setting parameter as False help to keep control on executions
with DAG('user_processing', start_date=datetime(2022, 8, 24), schedule_interval='@daily', catchup=False) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',  # on Airflow UI Admin-Connections-New Connection
        sql='''
        CREATE TABLE IF NOT EXISTS users (
          firstname TEXT NOT NULL,
          lastname TEXT NOT NULL,
          country TEXT NOT NULL,
          username TEXT NOT NULL,
          password TEXT NOT NULL,
          email TEXT NOT NULL  
        );
        '''
    )

# ACCES AIRFLOW CLI
# Test dags:
# Enter Docker CLI:
# docker exec -i -t materials-airflow-scheduler-1 /bin/bash

# TASK TEST:

# airflow tasks test user_processing create_table 2022-08-24

# ctrl + d to exit
