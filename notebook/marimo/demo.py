import marimo

__generated_with = "0.19.9"
app = marimo.App(width="full")

with app.setup:
    import pathlib
    from pathlib import Path
    import os, sys, pathlib, importlib.util

    # JAVA_HOME = "./source/jdk-17.0.10+7"
    # os.environ["JAVA_HOME"] = JAVA_HOME
    # os.environ["PATH"] = f"{JAVA_HOME}/bin:" + os.environ.get("PATH", "")

    spec = importlib.util.find_spec("pyspark")
    pyspark_home = str(pathlib.Path(spec.origin).parent) 
    os.environ["SPARK_HOME"] = pyspark_home

    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

    tmp = os.path.expanduser("~/tmp/pyspark")
    os.makedirs(tmp, exist_ok=True)
    os.environ["TMPDIR"] = tmp
    os.environ["SPARK_LOCAL_DIRS"] = tmp
    os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"
    os.environ["PYSPARK_VERBOSE"] = "1"

    from pyspark.sql import SparkSession, Row, functions as F, types as T
    from pyspark.sql.functions import pandas_udf
    from pyspark.sql import functions as F, Window

    import marimo as mo
    import marimo_lib as molib
    import spark_oedo.bin as decode 
    import spark_hh015


@app.cell
def _():
    _basedir = './rawdata/'
    _input = 'run001077.parquet'

    _input_info = [
        "mwdc_processor.py",
        _basedir + _input,
        "--output-wire-data",
        "--spark-oedo-jar",
        "/Users/fendo/Work/Program/uv-python/spark-oedo/src/spark_oedo/scala_package/target/scala-2.13/spark-oedo-package_2.13-1.0.jar"
    ]

    sys.argv =_input_info

    spark_hh015.mwdc_processor.main()
    return


@app.cell
def _():
    spark = SparkSession.builder.master("local[*]") \
            .config("spark.driver.memory","20g") \
            .config("spark.executor.memory","20g") \
            .config("spark.sql.shuffle.partitions","32") \
            .config("spark.jars","/home/h487/opt/spark-oedo/scala_package/target/scala-2.13/spark-oedo-package_2.13-1.0.jar,/home/h487/opt/rapids/rapids-4-spark_2.13-25.10.0.jar") \
            .config("spark.rapids.sql.explain","NONE") \
            .config("spark.rapids.sql.concurrentGpuTasks","2") \
            .config("spark.rapids.memory.pinnedPool.size","2g") \
            .config("spark.sql.files.maxPartitionBytes","512m") \
            .config("spark.kryo.registrator","com.nvidia.spark.rapids.GpuKryoRegistrator") \
            .config("spark.plugins","com.nvidia.spark.SQLPlugin") \
            .config("spark.rapids.memory.gpu.allocFraction","0.3") \
            .config("spark.rapids.memory.gpu.minAllocFraction","0.01") \
            .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    # rawdata/run001077_mwdc.parquet
    df = spark.read.parquet('/Users/fendo/tmp/hh015/nestdaq-data/run001077_mwdc.parquet')
    return (df,)


@app.cell
def _(df):
    df.printSchema()
    return


@app.cell
def _(df):
    _data_labels = [
        "hbfNumber",
        "dc31_x1_id",
        "dc31_x1_timing",
        "dc31_x1_charge"
    ]

    df.select(_data_labels).show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
