from airflow.sdk import dag, task
from datetime import datetime, timedelta

# Default args for tasks
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# DAG using decorator
@dag(
    dag_id="python_decorator_dag",
    default_args=default_args,
    description="A non-Spark DAG using decorators",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
)
def python_pipeline():

    @task()
    def extract():
        data = ["zak", "airflow", "docker"]
        print(f"Extracted data: {data}")
        return data

    @task()
    def transform(data):
        transformed = [s.upper() for s in data]
        print(f"Transformed data: {transformed}")
        return transformed

    @task()
    def load(transformed_data):
        print(f"Loading data: {transformed_data}")
        return True

    # Task dependencies
    data = extract()
    transformed = transform(data)
    load(transformed)

# Instantiate DAG
dag = python_pipeline()