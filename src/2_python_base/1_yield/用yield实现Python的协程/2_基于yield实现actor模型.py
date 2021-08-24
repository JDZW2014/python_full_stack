# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-08-24
Description :
auther : wcy
"""
# import modules
import os

__all__ = []


# define class
class ActorScheduler(object):
    """
    控制事件循环
    """
    def __init__(self):
        self._actor = {}
        self._msg_queue = list()

    def add_actor(self, name, actor):
        self._msg_queue.append((actor, None))
        self._actor[name] = actor

    def push(self, name, msg):
        actor = self._actor.get(name)
        self._msg_queue.append((actor, msg))

    def pop(self):
        actor, msg = self._msg_queue.pop(0)
        return actor, msg

    def have_task(self):
        return len(self._msg_queue) > 0

    def run(self):
        while self.have_task():
            actor, msg = self.pop()
            try:
                task_name = actor.send(msg)
            except:
                print("{} 任务终止".format(task_name))


# define function
def task_func(task_name):
    while True:
        num = yield task_name
        print("{} : {}".format(task_name, num))


def counter(actor_scheduler: ActorScheduler):
    while True:
        n = yield "counter"
        print("counter : {}".format(n))
        actor_scheduler.push(name="task1", msg=n)
        actor_scheduler.push(name="task2", msg=n)
        if n <= 0:
            break
        actor_scheduler.push(name="counter", msg=n-1)


def main():
    actor_scheduler = ActorScheduler()

    actor_scheduler.add_actor(name="task1", actor=task_func(task_name='t1'))
    actor_scheduler.add_actor(name="task2", actor=task_func(task_name='t2'))
    actor_scheduler.add_actor(name="counter", actor=counter(actor_scheduler=actor_scheduler))

    actor_scheduler.push(name="counter", msg=10)
    actor_scheduler.run()


# main
if __name__ == '__main__':
    main()
