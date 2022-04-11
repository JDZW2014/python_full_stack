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
def start_server(port: int) -> typing.NoReturn:
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind((socket.gethostname(), port))
    s.listen(backlog=5)
    while 1:
        conn, addr = s.accept()
        msg = conn.recv(1024)
        conn.send("receive msg : {}".format(msg.decode()).encode("utf-8"))
        conn.close()


# main
if __name__ == '__main__':
    start_server(port=8080)
