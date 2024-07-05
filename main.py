
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("PySparkApp") \
    .getOrCreate()