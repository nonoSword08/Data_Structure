# -*- coding: utf-8 -*-
"""
__mktime__ = '2019/4/25 0025'
__author__ = 'Administrator'
__filename__ = 'stack_test'
文件注解：
"""


class SStack(object):
    """
    使用顺序表的方式实现栈
    """

    def __init__(self):
        self.__elements = []

    def is_empty(self):
        """
        判断是否是空栈
        :return: 返回布尔
        """
        return self.__elements == []

    def push(self, value):
        """
        压栈操作
        :param value:
        :return:
        """
        self.__elements.append(value)

    def pop(self):
        """
        弹出最后一个元素
        :return: 返回pop的元素值
        """
        return self.__elements.pop()

    def top(self):
        """
        返回栈顶元素值
        :return:
        """
        return self.__elements[-1]

    def get_size(self):
        """
        获取栈长度
        :return:
        """
        return len(self.__elements)


if __name__ == '__main__':
    s = SStack()
    print(s.is_empty())
    s.push(123)
    s.push(456)
    print(s.get_size())
    print(s.top())
    print(s.pop())
    print(s.top())
