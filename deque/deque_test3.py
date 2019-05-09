#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
对于一对正整数a,b,对a只能进行加1，减1，乘2操作，问最少对a进行几次操作能得到b？提示：可以使用广度优先搜索，寻找a到b状态迁移的最短路径
"""

from collections import deque

# class MinPath(object):




def func1(a, targe):
    deque_list = [deque([targe])]
    # while True:
    for num_deque in deque_list:
        if num_deque[-1] % 2 == 0:
            num_deque.append(num_deque[-1] // 2)
        else:
            deque_list.append(num_deque.copy())
            num_deque.append(num_deque[-1] - 1)
            num_deque.append(num_deque[-1] + 1)
    print(deque_list)


    # if target % 2 == 0:
    #     if target == 2:
    #         return num_deque
    #     num_deque.append(target // 2)
    #     func1(a, target // 2, num_deque)
    #     return num_deque
    # else:
    #     target1 = target - 1
    #     if target1 == 2:
    #         return num_deque
    #     num_deque.append(target1 // 2)
    #     func1(a, target1 // 2, num_deque)
    #     return num_deque
    #     target2 = target + 1
    #     if target2 == 2:
    #         return num_deque
    #     num_deque.append(target2 // 2)
    #     func1(a, target2 // 2, num_deque)
    #     return num_deque


if __name__ == '__main__':
    func1(2, 1023)
