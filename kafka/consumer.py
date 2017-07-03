from kafka import KafkaConsumer
import pickle

# 读取数据
consumer = KafkaConsumer('network-monitor')
# print(pickle.loads(next(consumer).value))
for msg in consumer:
    print(pickle.loads(msg.value))
