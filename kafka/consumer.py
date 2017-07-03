# -*- coding: utf-8 -*-

from kafka import KafkaConsumer
import pickle

# 读取数据
consumer = KafkaConsumer('network-monitor', bootstrap_servers=['192.168.33.31:9092', '192.168.33.31:9093'])
# print(pickle.loads(next(consumer).value))
for msg in consumer:
    print(pickle.loads(msg.value))
