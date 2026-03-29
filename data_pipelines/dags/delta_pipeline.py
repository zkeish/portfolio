from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

with DAG(
    dag_id="delta_lake_pipeline",
    start_date=datetime(2026, 3, 28),
    schedule=None,
    catchup=False,
) as dag:

    spark_submit = SparkSubmitOperator(
        task_id="run_delta_job",
        application="/opt/airflow/spark_jobs/delta_job.py",
        conn_id="spark_default",
        spark_binary="/opt/spark/bin/spark-submit",
        verbose=True,
    )