from airflow.sdk import dag, task
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

# Default args
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 0
}

# DAG using decorator
@dag(
    dag_id="spark_delta_decorator_dag",
    default_args=default_args,
    description="A DAG using decorators to submit Spark jobs",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
)
def spark_delta_pipeline():

    # Task: Submit Spark Job
    spark_submit_task = SparkSubmitOperator(
        task_id="run_delta_job",
        application="./spark_jobs/delta_job.py",
        conn_id="spark_default"
    )

    return spark_submit_task

# Instantiate the DAG
dag = spark_delta_pipeline()