import time
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

class PySparkHelper:
    def __init__(self, spark: SparkSession):
        """
        Initialize the helper class with a SparkSession.
        """
        self.spark = spark

    @staticmethod
    def time_it(func):
        """
        A decorator to measure the time a function takes to run.
        """
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Execution time for {func.__name__}: {end_time - start_time:.2f} seconds")
            return result
        return wrapper

    def read_parquet(self, path: str) -> DataFrame:
        """
        Reads a Parquet file and returns a DataFrame.
        """
        print(f"Reading Parquet file from: {path}")
        return self.spark.read.parquet(path)

    @time_it
    def cache_df(self, df: DataFrame) -> DataFrame:
        """
        Caches a DataFrame to avoid re-computation.
        """
        print("Caching DataFrame")
        df.cache()
        return df

    @time_it
    def persist_df(self, df: DataFrame, storage_level="MEMORY_AND_DISK") -> DataFrame:
        """
        Persists a DataFrame with a specified storage level.
        Default is MEMORY_AND_DISK.
        """
        from pyspark import StorageLevel
        level = getattr(StorageLevel, storage_level)
        print(f"Persisting DataFrame with storage level: {storage_level}")
        df.persist(level)
        return df

    @time_it
    def drop_null_columns(self, df: DataFrame, threshold: float = 0.7) -> DataFrame:
        """
        Drops columns from a DataFrame if more than a certain percentage of values are null.
        """
        total_rows = df.count()
        for col_name in df.columns:
            null_count = df.filter(col(col_name).isNull()).count()
            null_ratio = null_count / total_rows
            if null_ratio > threshold:
                print(f"Dropping column {col_name} with {null_ratio:.2%} nulls")
                df = df.drop(col_name)
        return df

    @time_it
    def write_df(self, df: DataFrame, path: str, format: str = 'parquet', mode: str = 'overwrite'):
        """
        Writes the DataFrame to the given path in the specified format.
        Supported formats: parquet, csv, json
        """
        print(f"Writing DataFrame to {path} as {format}")
        if format == 'parquet':
            df.write.mode(mode).parquet(path)
        elif format == 'csv':
            df.write.mode(mode).csv(path, header=True)
        elif format == 'json':
            df.write.mode(mode).json(path)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def print_schema(self, df: DataFrame):
        """
        Prints the schema of a DataFrame in a readable format.
        """
        print("Schema of DataFrame:")
        df.printSchema()

    @time_it
    def show_df(self, df: DataFrame, num_rows: int = 20):
        """
        Shows the specified number of rows from the DataFrame.
        """
        print(f"Showing {num_rows} rows of DataFrame:")
        df.show(num_rows, truncate=False)

# Example usage:
'''
if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("PySpark Helper Demo") \
        .getOrCreate()

    helper = PySparkHelper(spark)
    
    # Reading a Parquet file
    df = helper.read_parquet("/path/to/parquet/file")
    
    # Caching the DataFrame
    df = helper.cache_df(df)
    
    # Dropping columns with more than 70% nulls
    df = helper.drop_null_columns(df, threshold=0.7)
    
    # Writing the DataFrame as parquet
    helper.write_df(df, "/path/to/output/dir", format="parquet")
    
    # Displaying the schema and a sample of the DataFrame
    helper.print_schema(df)
    helper.show_df(df, num_rows=10)
'''