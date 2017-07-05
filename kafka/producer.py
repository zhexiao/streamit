# -*- coding: utf-8 -*-
from kafka import KafkaProducer
import time
import pickle
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093'])

i = 0
while True:
    i += 1
    data = {
        'key': 'test',
        'val': i
    }

    # 二进制传输数据
    # producer.send('my-replicated-topic', pickle.dumps(data))

    # json编码传输
    producer.send('my-replicated-topic', json.dumps(data).encode('utf-8'))

    time.sleep(2)
