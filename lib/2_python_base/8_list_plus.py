# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-02-02
Description : 重新包装 list 类，练习 类的内置方法
auther : wcy
"""
# import modules
import typing

__all__ = []


# define class
class List(list):
    def __init__(self, name: str, age: int, data: typing.List) -> typing.NoReturn:
        super().__init__(data)
        self.__dict__["name"] = name
        self.__dict__["age"] = age
        print("init finish")
        pass

    def __getattr__(self, item) -> typing.NoReturn:
        """
        only triggered when item attribute not exits
        """
        print("cat not find {0}, return None".format(item))
        return None

    def __setattr__(self, key: str, value: int) -> bool:
        if isinstance(key, str) and isinstance(value, int):
            self.__dict__[key] = value
            return True
        else:
            print("key type is {0}, value type is {1}, set attr fail".format(type(key), type(value)))
            return False

    def __delattr__(self, item: str) -> bool:
        self.__dict__.pop(item)
        return True

    def __getitem__(self, item: str) -> typing.NoReturn:
        """
        only triggered when item not exits
        """
        print("can not find {0}, return None".format(item))
        return None

    def __setitem__(self, key: str, value: str) -> typing.NoReturn:
        if isinstance(key, str) and isinstance(value, str):
            self.__dic__[key] = value
            return True
        else:
            print("key type is {0}, value type is {1}, set attr fail".format(type(key), type(value)))
            return False

    def __delitem__(self, key: str) -> bool:
        self.__dict__.pop(key)
        return True

    def __del__(self) -> bool:
        print("the class will cleared, the dict is : ")
        print(self.__dict__)
        return True

    def __call__(self, call_string: str, *args, **kwargs) -> typing.NoReturn:
        print("the class is called, call_string is {}".format(call_string))

    def __str__(self):
        return "from __str__: name is {}, age is {}".format(self.name, self.age)

    def __repr__(self):
        return "from __repr: name is {}, age is {}".format(self.name, self.age)


class BaseClass(object):
    __slots__ = ["name", "age"]


class Test1(object):
    pass


# define func
def print_wrapper_wrapper():
    def print_wrapper():
        def wrapper():
            pass
        return print_wrapper

    return print_wrapper


# main
if __name__ == "__main__":
    print("-" * 20)
    l = List(name="aaa", age=10, data=[1, 2, 3])
    l(call_string="test __call__ func")
    print("-" * 20)
    print(l.name)
    print(l.a)
    print("-" * 20)
    l.a = 0
    l["a"] = "1"
    print("-" * 20)
    print(l["aa"])



