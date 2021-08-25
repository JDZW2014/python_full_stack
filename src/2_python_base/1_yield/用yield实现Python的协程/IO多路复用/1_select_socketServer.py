# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-08-24
Description :
auther : wcy
"""
# import modules
import os
import select
import socket
import queue

__all__ = []


# define class
class UnblockSocketTest(object):
    def __init__(self, addr, port):
        self.server = socket.socket()
        self.server.bind(address=(addr, port))
        self.server.listen(1024)
        self.server.setblocking(False)

        self.msg_dict = dict()
        self._inputs = []
        self._outputs = []

    def add_monitor_server(self, s):
        self._inputs.append(s)

    def run(self):
        while self._inputs:
            print("waiting ...")
            read_list, write_list, error_list = select.select(self._inputs, self._outputs, self._inputs)
            # todo 看完socket 编程后完成这一部分
            if read_list:
                self._deal_read_list(deal_list=read_list)
            if write_list:
                self._deal_write_list(deal_list=write_list)
            if error_list:
                self._deal_error_list(deal_list=error_list)

    def _deal_read_list(self, deal_list):
        print(" -- deal read list ---")
        pass

    def _deal_write_list(self, deal_list):
        print(" -- deal write list ---")
        pass

    def _deal_error_list(self, deal_list):
        print(" -- deal error list ---")
        pass


# define function
def main():
    pass


# main
if __name__ == '__main__':
    main()
