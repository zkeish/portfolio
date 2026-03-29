from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="spark_example",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["example"],
) as dag:
    run_spark = BashOperator(
        task_id="run_spark_example",
        bash_command="echo 'Spark container is available at spark:4040'",
    )

    run_spark
