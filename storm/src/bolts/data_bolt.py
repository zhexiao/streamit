import os
from streamparse import Bolt


class DataBolt(Bolt):
    # 如果需要从bolt继续传输数据到另一个bolt，则定义outputs与emit
    # outputs = ['word']

    def initialize(self, conf, ctx):
        self.pid = os.getpid()

    def process(self, tup):
        """
        对传来的数据进行处理
        :param tup:
        :return:
        """
        val = tup.values[0]

        self.logger.info('value ----- {}, tuple----{}, pid={}'.format(
            val, tup, self.pid
        ))

        # 如果需要从bolt继续传输数据到另一个bolt，则定义outputs与emit
        # self.emit([word])
