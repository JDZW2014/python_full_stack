# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-01-26
Description :
auther : wcy
"""
# import modules
import logging

__all__ = []


# define function
def log_basic_config():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logging.basicConfig(
        filename="log_basic_config.log",
        filemode="a",
        format="%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s"
    )

    logger.info("log_basic_config")


def logging_more():
    # logger, handler, filter, formatter 是 logging 模块的四个基本概念
    # logger
    # 日志记录器，树形层级结构， debug, info, warning, error, critical， 多次使用相同的name 会发返回一个下相同的logger对象
    logger = logging.getLogger()

    # formatter
    # 日志的格式，定义信息格式和时间格式
    fmt = logging.Formatter()

    # handler 将日志内容通过handler 发送到合适的输出
    # Handler -> StreamHandler -> FileHandler
    # https://www.cnblogs.com/zhangliang91/p/11920643.html
    sh = logging.StreamHandler()
    fh = logging.FileHandler()
    nh = logging.NullHandler()

    # filter， 决定一个日志是否发送到handler
    log_filter = logging.Filter()





# main
if __name__ == '__main__':
    pass