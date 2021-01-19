# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-01-18
Description : 用装饰器给函数添加  用户密码登录功能
auther : wcy
"""
# import modules

__all__ = ["login_wrapper"]


# user login info
LOGIN_INFO1 = {"test1": "test1_pwd",
               "test2": "test2_pwd",
               "test3": "test3_pwd",
               "test4": "test4_pwd"}

LOGIN_INFO2 = {"test1": "test1_pwd1",
               "test2": "test2_pwd2",
               "test3": "test3_pwd3",
               "test4": "test4_pwd4"}

LOGIN_STATUS = False


# define function
def login_wrapper(notification_type: int):
    if notification_type == 1:
        login_info = LOGIN_INFO1
    elif notification_type == 2:
        login_info = LOGIN_INFO2
    else:
        raise ValueError("wrong notification_type: {}".format(notification_type))

    def login_wrapper_func(func):
        def wrapper(*args, **kwargs):
            global LOGIN_STATUS
            if LOGIN_STATUS:
                return func(*args, **kwargs)
            else:
                name = input("input name: ")
                pwd = input("input pwd: ")

                if login_info[name] == pwd:
                    LOGIN_STATUS = True
                    return func(*args, **kwargs)
                else:
                    print("wrong pwd or name")
        return wrapper

    return login_wrapper_func


@login_wrapper(notification_type=1)
def main_page():
    print("成功打开 main_page")
    pass


@login_wrapper(notification_type=1)
def page_info():
    print("成功打开 page_info")
    pass


@login_wrapper(notification_type=1)
def similar_goods():
    print("成功打开 similar_goods")
    pass


# main
if __name__ == "__main__":
    main_page()
    page_info()