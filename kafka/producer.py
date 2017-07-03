# -*- coding: utf-8 -*-
from kafka import KafkaProducer
import time
import pickle

producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093'])

i = 0
while True:
    i += 1
    data = {
        'key': 'test',
        'val': i
    }

    # 二进制传输数据
    producer.send('network-monitor', pickle.dumps(data))

    time.sleep(2)
