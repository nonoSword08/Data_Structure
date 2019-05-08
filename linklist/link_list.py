# -*- coding: utf-8 -*-
"""
__mktime__ = '2019/4/24 0024'
__author__ = 'Administrator'
__filename__ = 'link_list'
文件注解：
"""


class Node(object):
    # 定义node
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_value(self, new_value):
        self.value = new_value

    def set_next(self, new_next):
        self.next_node = new_next


# 定义链表
class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def add(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.head = node
        self.length += 1

    def get_list(self):
        cur = self.head
        print(cur.get_value())
        while cur.get_next():
            cur = cur.get_next()
            print(cur.get_value())

    def append(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
        else:
            cur = self.head
            while cur.get_next():
                cur = cur.get_next()
            cur.set_next(node)
        self.length += 1

    def search(self, value):
        """

        :param value: 在链表中查找的值
        :return:
        """
        pass

    def insert(self, new_value, value, count):
        """
        在链表中插入新的节点
        :param new_value: 新节点的值
        :param value: 在第count次查到到value的值后插入
        :param count: value出现的次数
        :return:
        """
        pass

    def remove(self, value):
        """
        删除节点
        :param value: 要删除有该值的节点，删除第一次出现该值的节点
        :return:
        """
        pass


link = LinkList()
link.add(1)
link.add(2)
link.get_list()


