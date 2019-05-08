# -*- coding: utf-8 -*-
"""
__mktime__ = '2019/4/25 0025'
__author__ = 'Administrator'
__filename__ = 'stack_test2'
文件注解：
"""


class Node(object):
    # 定义node
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LStack(object):
    """
    使用链表的方式实现栈
    节点就是讲的node
    """

    def __init__(self):
        self.__top = None

    def is_empty(self):
        """
        判断是否是空栈
        :return: 返回布尔
        """
        return self.__top is None

    def push(self, value):
        """
        压栈操作
        :param value:
        :return:
        """
        self.__top = Node(value, self.__top)

    def pop(self):
        """
        如果是空栈
        :return: 返回pop的元素值
        """
        if self.is_empty():
            raise IndexError('stack is empty')

        else:
            val = self.__top.value
            self.__top = self.__top.next_node
            return val

    def top(self):
        """
        返回栈顶元素值
        :return:
        """
        return None if self.is_empty() else self.__top.value

    def get_size(self):
        """
        获取栈长度
        :return:
        """
        num = 0
        temp = self.__top
        while temp is not None:
            temp = temp.next_node
            num += 1
        return num


# 括号匹配问题
def func(string):
    s1 = LStack()
    brackets_list1 = ['(', '[', '{']
    brackets_list2 = [')', ']', '}']
    for i in range(len(string)):
        si = string[i]
        if si not in brackets_list1 or si not in brackets_list2:
            continue
        if si in brackets_list1:
            s1.push(si)
        if s1.is_empty():
            return False
        p = s1.pop()
        if (p == '(' and si == ')') or (p == '[' and si == ']') or (p == '{' and si == '}'):
            continue
        else:
            return False
    if s1 != 0:
        return False
    return True




if __name__ == '__main__':
    s = LStack()
    print(s.is_empty())
    s.push(123)
    s.push(456)
    s.push(789)
    s.push(112233)
    print(s.is_empty())
    print(s.get_size())
    print(s.top())
    print(s.pop())
    print(s.top())
