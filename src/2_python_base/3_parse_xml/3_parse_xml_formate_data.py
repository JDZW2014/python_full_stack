# !/user/bin/python
# -*- coding:utf-8 -*-
"""
date：          2021-01-22
Description :
auther : wcy
"""
# import modules
import os
import xml.etree.ElementTree as ET

__all__ = []


# define function
def parse_data(file_path: str) -> None:
    tree = ET.ElementTree(file=file_path)
    t_r = tree.getroot()
    print(t_r.tag)
    for data in t_r:
        print(data.tag, data.attrib, data.text)
        for dat in data:
            pass


def parse_to_json_recur(data_path):
    pass


def write_data(file_path: str) -> None:
    pass


# main
if __name__ == '__main__':
    # parse_data(file_path="3_data.xml")
    pass