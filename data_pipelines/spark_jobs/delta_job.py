from pyspark.sql import SparkSession
from auto_cdc import CDC
from datetime import datetime

spark = (
    SparkSession.builder
    .appName("airflow-delta")
    .config("spark.sql.warehouse.dir", "/opt/spark/warehouse") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.sql.catalogImplementation", "hive") \
    .enableHiveSupport() \
    .getOrCreate()
)

data = [("Alice", 34), ("Bob", 45)]
df = spark.createDataFrame(data, ["name", "age"])

# spark.sql("CREATE DATABASE IF NOT EXISTS test")
# spark.sql('create schema if not exists test')
# df.write.format("delta").mode("overwrite").saveAsTable('test.raw')

spark.sql('select * from test.raw')
# CDC.write_to_cdc_feed(df, '/sbx/raw/testing/data/', ['name'], datetime.now())

df.show()

spark.stop()

print('hello world')