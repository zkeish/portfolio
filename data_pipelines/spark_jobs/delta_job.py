from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TestJob").getOrCreate()

# data = [("Alice", 34), ("Bob", 45)]
# df = spark.createDataFrame(data, ["name", "age"])

# df.show()

# spark.stop()

print('hello world')