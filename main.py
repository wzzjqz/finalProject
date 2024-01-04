import urllib
from urllib.parse import quote_plus
from pymongo import MongoClient
import random
import time

username = "admin"
database_name = "root"
password = "1234567wzy@"
port = 3717
host = 'dds-bp1fefdb61bbbe041.mongodb.rds.aliyuncs.com'
client = MongoClient('mongodb://{0}:{1}@{2}:{3}'.format(urllib.parse.quote_plus(username),urllib.parse.quote_plus(password),host,port))

database = client["temperature_database"]
collection = database["temperature_collection"]

def generate_random_data():
    # 生成合理范围内的温度和湿度数据
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(40.0, 60.0), 2)
    return temperature, humidity

def insert_data_into_db():
    # 随机生成数据并插入数据库
    temperature, humidity = generate_random_data()
    data = {"temperature": temperature,  "humidity": humidity}
    collection.insert_one(data)

if __name__ == "__main__":
    while True:
        insert_data_into_db()
        print("1")
        time.sleep(60)  # 休眠60秒
