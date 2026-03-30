docker compose up postgres -d
docker compose run airflow-webserver airflow db migrate
# docker compose up --build