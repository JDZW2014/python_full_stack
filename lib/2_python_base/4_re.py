# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-01-26
Description : 用正则表达式实现一个 计算器 的功能
auther : wcy
"""
# import modules
import re

__all__ = ["calculator"]


# define function
def calculator():
    while 1:
        cal_str = input("请输入计算表达式：")
        result = calculate(cal_str.replace(" ", ""))
        print("计算结果是:{}".format(result))


def calculate(cal_str: str) -> int:
    find_list = re.findall(r"\([^()]+\)", cal_str)
    if len(find_list) < 1:
        return eval(cal_str)
    else:
        for find in find_list:
            cal_str = cal_str.replace(find, str(eval(find)))
            return calculate(cal_str)

# test
def test():
    # cal_str = "2*(3+4)"
    # result = calculate(cal_str=cal_str)
    # print(result)
    calculator()


# main
if __name__ == '__main__':
    test()
    pass