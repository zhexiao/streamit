from streamparse import Spout
from kafka import KafkaConsumer
import pickle


class DataSpout(Spout):
    # emit输出数据的字段名，如果emit多个数据，则与outputs对应
    outputs = ['message']

    def initialize(self, stormconf, context):
        # 生成iterator
        self.consumer = KafkaConsumer('network-monitor', bootstrap_servers=[
            'localhost:9092', 'localhost:9093'
        ])

    def next_tuple(self):
        """
        发送数据
        :return:
        """

        # 对interator使用next方法读取数据
        data = pickle.loads(next(self.consumer).value)
        # 发送数据
        self.emit([data])
