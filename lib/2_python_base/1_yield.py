# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-01-18
Description : 使用 yield 写一个生产者消费者模型
auther : wcy
"""
# import modules
import time
import uuid
from collections.abc import Generator

__all__ = []


# define function
def productor_func():
    while True:
        print("正在生成新的任务：")
        time.sleep(1)
        task = uuid.uuid4().__str__()
        print("生成任务: {}".format(task))
        consumer_result = yield task
        print("上一个任务的 consume result is : {}".format(consumer_result))


def consumer_func(productor: Generator):
    consume_result = None
    while True:
        print("\n-------- 等待接收新的任务 --------")
        task = productor.send(consume_result)
        print("消费任务：{}".format(task))
        consume_result = "success"

# main
if __name__ == '__main__':
    productor = productor_func()
    consumer_func(productor=productor)
    pass