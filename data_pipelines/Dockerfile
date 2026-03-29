FROM apache/airflow:3.1.8-python3.12

USER root
RUN apt-get update && apt-get install -y default-jdk
USER airflow

RUN pip install apache-airflow-providers-apache-spark pyspark