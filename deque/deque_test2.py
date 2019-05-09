#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
某动物园搬家，要运走N种动物，老虎与狮子放在一起会大家，大象与犀牛放在一个笼子会打架，野猪和野狗放在一个笼子里会打架。
现在需要我们设计一个算法，使得装进同一个笼子的动物互相不打架。
"""
from collections import deque


def func(zoo_deque1):
    zoo_deque2 = deque(['flag'])
    while True:
        if len(zoo_deque1) == 0:
            break
        ani = zoo_deque1.pop()
        if ani in ['老虎', '大象', '野猪']:
            zoo_deque2.appendleft(ani)
        else:
            zoo_deque2.append(ani)
    return zoo_deque2




if __name__ == '__main__':
    zoo_deque = deque(['其他', '狮子', '大象', '其他', '其他', '老虎', '其他', '犀牛', '野猪', '其他', '野狗', '其他'])
    print(func(zoo_deque))


