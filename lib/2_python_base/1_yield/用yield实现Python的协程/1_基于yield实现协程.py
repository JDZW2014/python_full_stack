# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-08-23
Description :
auther : wcy
"""
# import modules

__all__ = []


# define class
class TaskScheduler(object):
    def __init__(self):
        self.task_queue = list()

    def push_task(self, t):
        self.task_queue.append(t)

    def pop_task(self):
        return self.task_queue.pop(0)

    def run(self):
        while self.task_queue:
            t = self.pop_task()
            try:
                t_name = next(t)
                self.push_task(t)
            except:
                print("{} 任务执行结束".format(t_name))


# define function
def task_func(n, task_name):

    num = 0
    while num < n:
        print("{} : {}".format(task_name, num))
        yield task_name
        num += 1


def main():
    task_scheduler = TaskScheduler()
    task_scheduler.push_task(task_func(n=10, task_name="task1_10"))
    task_scheduler.push_task(task_func(n=15, task_name="task2_15"))
    task_scheduler.run()


# main
if __name__ == '__main__':
    main()
