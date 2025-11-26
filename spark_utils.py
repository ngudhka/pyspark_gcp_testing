from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col
import pandas as pd
import matplotlib.pyplot as plt


def get_spark_session(app_name: str = "SparkApplication", master: str = "local[*]") -> SparkSession:
    """
    Initialises and returns a SparkSession.
    """
    print(f"Initialising SparkSession for '{app_name}' with master '{master}'...")
    return SparkSession.builder \
        .master(master) \
        .appName(app_name) \
        .getOrCreate()
        
def load_data(spark: SparkSession, file_path: str, file_format: str = "json", **options) -> DataFrame:
    """
    Loads data from a specified path into a Spark DataFrame.

    Args:
        spark (SparkSession): The active SparkSession.
        file_path (str): The path to the data file.
        file_format (str): The format of the file (e.g., "json", "csv").
        **options: Additional options for the reader (e.g., header=True for CSV).

    Returns:
        DataFrame: The loaded Spark DataFrame.
    """
    print(f"Loading {file_format} data from: {file_path}")
    return spark.read.format(file_format).options(**options).load(file_path)

def display_df_info(df: DataFrame, sample_rows: int = 5, truncate: bool = False) -> None:
    """
    Displays schema and a sample of the data.
    """
    print("\n--- DataFrame Schema ---")
    df.printSchema()
    print("\n--- Sample Data ---")
    df.show(sample_rows, truncate)
    print("------------------------")
    
def get_unique_values(df: DataFrame, column_name: str, order_by_count: bool = True, limit: int = None) -> DataFrame:
    """
    Returns unique values and their counts for a specified column.

    Args:
        df (DataFrame): The input Spark DataFrame.
        column_name (str): The name of the column.
        order_by_count (bool): If True, orders by count descending; otherwise, orders by column value.

    Returns:
        DataFrame: A DataFrame with unique values and their counts.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")

    print(f"Getting unique values and counts for column '{column_name}'...")
    if order_by_count:
        return df.groupBy(column_name).count().orderBy(col("count").desc())
    else:
        return df.groupBy(column_name).count().orderBy(column_name)


def plot_bar_chart(data_series, labels, title, x_label, y_label, color='skyblue', rotation=0, figsize=(10, 6)):
    """
    Generates a generic bar chart.
    Assumes data_series and labels are lists/pandas Series.
    """
    if not isinstance(data_series, pd.Series):
        data_series = pd.Series(data_series)
    if not isinstance(labels, pd.Series):
        labels = pd.Series(labels)

    plt.figure(figsize=figsize)
    plt.bar(labels, data_series, color=color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=rotation)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def group_and_aggregate(df: DataFrame, group_by_cols: list, agg_expressions: list, order_by_cols: list = None) -> DataFrame:
    """
    Performs a group by operation followed by custom aggregations.

    Args:
        df (DataFrame): The input Spark DataFrame.
        group_by_cols (list): List of column names to group by.
        agg_expressions (list): List of PySpark aggregation expressions (e.g., F.avg("col").alias("avg_col")).
        order_by_cols (list, optional): List of column names to order the final result by.

    Returns:
        DataFrame: The aggregated DataFrame.
    """
    if not isinstance(group_by_cols, list) or not group_by_cols:
        raise ValueError("group_by_cols must be a non-empty list of column names.")
    if not isinstance(agg_expressions, list) or not agg_expressions:
        raise ValueError("agg_expressions must be a non-empty list of PySpark aggregation expressions.")

    print(f"Grouping by {group_by_cols} and applying aggregations...")
    aggregated_df = df.groupBy(*group_by_cols).agg(*agg_expressions)
    
    if order_by_cols:
        print(f"Ordering by {order_by_cols}...")
        # Use col() for ordering to allow for desc() or asc() if needed,
        # but for simplicity here, we assume direct column names.
        aggregated_df = aggregated_df.orderBy(*order_by_cols)
        
    return aggregated_df
