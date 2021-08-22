# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-02-09
Description :
auther : wcy
"""
# import modules
import socket
import typing

__all__ = []


# define function
def start_client(msg: str, port: int) -> typing.NoReturn:
    client = socket.socket()
    client.connect((socket.gethostname(), port))
    client.send(msg.encode("utf8"))
    msg = client.recv(1024)
    print(msg.decode("utf-8"))


# main
if __name__ == '__main__':
    start_client(msg="hello", port=8080)
