# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2022-04-19
Description :
auther : wcy
"""
# import modules
import os

__all__ = []

"""
说明：
第一题：
    这个是位图的升级，方法不唯一：
        方法一： 讲位图从一个位来计数改为两个未来计数，
            0： 没出现过
            1： 出现过一次
            2： 出现过两次
            3： 出现过三次及以上
        方法二： 使用两个位图来计数，逻辑和方法一类似
第二题： 还是使用分桶统计的方法
"""
