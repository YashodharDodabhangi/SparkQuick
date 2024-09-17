from pyspark.sql import SparkSession
from dataclasses import dataclass



@dataclass
class pysparkHelper:
    spark:SparkSession
    
