# streamit

#### 安装Python及其依赖
```shell
> sudo apt-get install python3 python3-dev python3-pip
> sudo apt-get install libffi-dev libssl-dev
> sudo pip3 install virtualenv
```

#### Kafka 环境
```shell
# 启动 zookeeper
> ./bin/zookeeper-server-start.sh config/zookeeper.properties &

# 启动 kafka server 0
> ./bin/kafka-server-start.sh config/server.properties &

# 启动 kafka server 1
> ./bin/kafka-server-start.sh config/server-1.properties &
 
# 创建 topic
> ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 1 --topic network-monitor
 
# 检查 topic
> ./bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic network-monitor

> virtualenv -p python3 ~/env_kafka
> source ~/env_kafka/bin/activate
> pip install -r kafka/kafka_requirements.txt
```

#### Storm环境
```shell
# 安装 Leiningen
> wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
> sudo cp lein /usr/local/bin/
> sudo chmod a+x /usr/local/bin/lein
> lein
> lein version

# 链接 storm命令
> sudo ln -s /vagrant/apache-storm-1.1.0/bin/storm /usr/local/bin/
> storm version

> virtualenv -p python3 ~/env_storm
> source ~/env_storm/bin/activate
> pip install -r storm/storm_requirements.txt
```