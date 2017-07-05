# -*- coding: utf-8 -*-
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json


sc = SparkContext(master="local[2]", appName="spark_with_kafka_demo")
ssc = StreamingContext(sc, 5)

zookeeper_host = '192.168.33.31:2181'
group_ids = 'spark-kafka-consumer-demo'
topics = {
    'my-replicated-topic': 1
}

kvs = KafkaUtils.createStream(ssc, zookeeper_host, group_ids, topics)
data = kvs.map(lambda dt: dt[1])

data.pprint()

# counts = lines.flatMap(lambda line: line.split(" ")) \
#     .map(lambda word: (word, 1)) \
#     .reduceByKey(lambda a, b: a + b)
# counts.pprint()

ssc.start()
ssc.awaitTermination()
