#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import deque


"""
编写程序，求二项式系数表中(杨辉三角)第K层系列数
"""


def factorial(num, length):
    if length == 0:
        return 1
    return num * factorial(num - 1, length - 1)


def combination(n, m):
    return factorial(n, n - m) // factorial(n - m, n - m)


def yanghui_list(line_num):
    if line_num == 1:
        return [1]
    d = deque()
    for i in range(line_num):
        d.append(combination(line_num - 1, i))
    return d


if __name__ == '__main__':
    print(yanghui_list(7))
