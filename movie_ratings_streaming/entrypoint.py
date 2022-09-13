import logging

from pyspark.sql.session import SparkSession

from movie_ratings_streaming.config.config import read_config, read_source_avro_schema
from movie_ratings_streaming.stream import MovieRatingsStream

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    config = read_config()
    source_avro_schema = read_source_avro_schema()

    spark_session = SparkSession.builder.getOrCreate()

    MovieRatingsStream(config, source_avro_schema, spark_session).run()
