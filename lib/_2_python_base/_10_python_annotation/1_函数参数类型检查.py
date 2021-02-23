# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-02-10
Description :
auther : wcy
"""
# import modules
import functools
import typing
import inspect


__all__ = []


# define wrapper
def arg_type_check(func):
    msg = ('Expected type {expected!r} for argument {argument}, '
           'but got type {got!r} with value {value!r}')
    # 获取函数定义的参数
    sig = inspect.signature(func)
    parameters = sig.parameters  # 参数有序字典
    arg_keys = tuple(parameters.keys())  # 参数名称
    pass

    @functools.wraps(func)
    def wrawpper(*args, **kwargs):
        print(sig)
        print(parameters)
        print(arg_keys)
        for i, value in enumerate(args):
            assert isinstance(value, parameters[arg_keys[0]].annotation)

        for k, v in kwargs.items():
            pass


        return func(*args, **kwargs)

    return wrawpper


# define class
class A:
    pass


class B:
    pass


# define function
@arg_type_check
def test(arg1: str, arg2: typing.Union[float, dict], arg3: typing.Union[A, B]) -> B:

    return arg3

# main
if __name__ == '__main__':
    a = A()
    b = B()
    test("aaaa", arg2={}, arg3=a)