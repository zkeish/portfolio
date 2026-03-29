FROM apache/airflow:3.1.8-python3.12

USER root

RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-11-jdk && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-18-openjdk-arm64
ENV PATH=/home/airflow/.local/bin:$PATH

USER airflow
RUN pip install --user apache-airflow-providers-apache-spark pyspark