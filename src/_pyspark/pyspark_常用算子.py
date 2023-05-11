# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-08-26
Description :
auther : wcy
"""
# import modules
import os
from pyspark import SparkContext, SparkConf


__all__ = []


# define class
class SparkDemo(object):
    os.environ['JAVA_HOME'] = "/Library/Java/JavaVirtualMachines/jdk1.8.0_161.jdk/Contents/Home"
    os.environ['SPARK_HOME'] = '/Users/wcy/2_myself_learn/python_full_stack/spark-1.6.0-bin-hadoop2.4'
    os.environ["PYSPARK_PYTHON"] = "/Users/wcy/anaconda3/envs/spark_3.5/bin/python"
    os.environ["PYSPARK_DRIVER_PYTHON"] = "/Users/wcy/anaconda3/envs/spark_3.5/bin/python"

    def __init__(self, app_name='test', master="local"):
        """
        local 模式, local[1], local 一个并行来跑， local[2] local 2个并行来跑
        yarn-master 模式
        yarn-client 模式
        """
        self.conf = SparkConf().setAppName(app_name).setMaster(master)
        self.sc = SparkContext(conf=self.conf)

    def task1_word_count(self):
        word_list = ["/Users/wcy/anaconda3/envs/spark_3.5/bin/python", '/Users/wcy/2_myself_learn/python_full_stack/spark-1.6.0-bin-hadoop2.4']
        rdd = self.sc.parallelize(word_list)
        rdd = rdd.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a+b)
        print(rdd.collect())

    def task2(self):
        pass

    def task3(self):
        pass


# main
if __name__ == '__main__':
    spark_demo = SparkDemo()
    spark_demo.task1_word_count()
