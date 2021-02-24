# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-02-23
Description :
auther : wcy
"""
# import modules
import _2_python_base._5_logging_src as logging

__all__ = []


# define function
def main(name):
    logger = logging.getLogger(name=name)
    # 执行流程：


# main
if __name__ == '__main__':
    main(name="root")
    main(name="demo")
    pass
