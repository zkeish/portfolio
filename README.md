# data_pipelines

This project contains an Airflow-based data pipeline environment with Spark and Delta Lake support.

## Overview

The `data_pipelines` folder defines a Docker Compose environment for running:

- Apache Airflow (webserver, scheduler, worker, dag processor, triggerer, and init service)
- PostgreSQL metadata database
- Redis broker for CeleryExecutor
- Apache Spark standalone cluster (master + worker)
- Delta Lake storage in a Docker volume

It includes two example Airflow DAGs:

- `python_decorator_dag`: a simple Python task-based DAG demonstrating extract/transform/load logic using Airflow decorators
- `spark_delta_decorator_dag`: a SparkSubmit DAG that runs a PySpark Delta Lake job defined in `spark_jobs/delta_job.py`

## Key Files

- `docker-compose.yml`: defines all services for Airflow, Spark, Redis, and PostgreSQL
- `Dockerfile`: custom Airflow image that installs Spark and Delta Lake dependencies
- `setup.sh`: helper script for local environment setup and launching Airflow
- `requirements.txt`: Airflow Spark provider dependency
- `dags/python_decorator_dag.py`: Python-based Airflow DAG
- `dags/spark_delta_decorator_dag.py`: Spark submit DAG
- `spark_jobs/delta_job.py`: PySpark job that demonstrates Delta Lake usage
- `config/airflow.cfg`: Airflow configuration mounted into the container

## Architecture

The environment is designed to run Airflow and Spark together:

- Airflow tasks are defined in `dags/`
- Spark jobs live in `spark_jobs/`
- The custom Docker image installs:
  - `apache-airflow-providers-apache-spark`
  - `pyspark==4.1.0`
  - `delta-spark==4.1.0`
  - `auto-cdc`
- Delta Lake storage is persisted in `delta-warehouse`

## DAGs

### `python_decorator_dag`

This DAG is a pure Python workflow using Airflow task decorators:

1. `extract()` creates a small list
2. `transform(data)` uppercases the items
3. `load(transformed_data)` prints the transformed output

It is configured with:

- `schedule=None`
- `catchup=False`
- retry settings via `default_args`

### `spark_delta_decorator_dag`

This DAG uses `SparkSubmitOperator` to submit a Spark job:

- `application`: `./spark_jobs/delta_job.py`
- `conn_id`: `spark_default`
- Delta Lake config options added via `conf`

The Spark job creates a Spark session configured for Delta Lake and runs a sample query.

## Running the project

From the `data_pipelines` directory, start the Docker Compose stack:

```bash
cd /Users/zkeish/repos/portfolio/data_pipelines
docker compose up --build
```

Once the environment is up, open the Airflow UI at:

- `http://localhost:8080`

## Recommended setup workflow

For a fresh start, run:

```bash
docker compose down -v
docker compose up postgres -d
docker compose run airflow-webserver airflow db migrate
docker compose up --build --remove-orphans
```

## Notes

- Airflow is configured to use `CeleryExecutor` with Redis and PostgreSQL.
- Spark is launched via standalone master/worker containers.
- Delta Lake storage is shared using the `delta-warehouse` Docker volume.
- `spark_jobs/delta_job.py` currently contains example Delta and CDC code; it can be updated for custom ETL logic.

## Helpful paths

- Airflow DAGs: `./dags`
- Spark applications: `./spark_jobs`
- Airflow config: `./config/airflow.cfg`
- Persistent logs: `./logs`

## Troubleshooting

- If Airflow services fail to start, check logs under `./logs` and container logs from Docker.
- Ensure Docker has enough memory (at least 4GB) and CPU resources for Spark and Airflow.
- If permission issues occur on Linux, set `AIRFLOW_UID` in an `.env` file or environment before starting.
