from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

sc = SparkContext(master="local[2]", appName="spark_with_kafka_demo")
ssc = StreamingContext(sc, 5)

zookeeper_host = '192.168.33.31:2181'
group_ids = 'spark-kafka-consumer-demo'
topics = {
    'network-monitor': 1
}
kafkaStream = KafkaUtils.createStream(ssc, zookeeper_host, group_ids, topics)
parsed = kafkaStream.map(lambda v: json.loads(v[1]))
print(parsed)

ssc.start()
ssc.awaitTermination()