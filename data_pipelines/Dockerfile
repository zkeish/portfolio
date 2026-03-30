FROM apache/airflow:3.1.8-python3.10

USER root
RUN apt-get update && apt-get install -y default-jdk && apt-get clean
USER airflow

RUN pip install \
    apache-airflow-providers-apache-spark \
    pyspark==4.0.2 \
    delta-spark