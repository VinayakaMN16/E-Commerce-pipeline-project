from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Reading E-Commerce Dataset")

def transform():
    print("Creating Fact Sales Table")

def load():
    print("Loading Data Into BigQuery")

with DAG(
    dag_id="ecommerce_pipeline",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load_bigquery",
        python_callable=load
    )

    extract_task >> transform_task >> load_task