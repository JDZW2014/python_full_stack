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
方法解读：
问题一：
    1. 如果可以容许错误率，可以使用布隆过滤器
    2. 使用位图：
        需要 100亿个比特位， 大约是 10 * 2**30 需要 1G 多的内存，不超过 2G
    3. 使用 hash 分桶
        单独找每个通中重复的url
    
    资源问题需要问清具体要求（是否容许失误率等），资源限制（内存大小）

问题二：
    1. hash 分桶，每个桶求top100, 然后个top k 维持一个大顶堆，每次各pop 一个，对比，汇总统计

"""
