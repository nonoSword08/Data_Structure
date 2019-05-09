#!/usr/bin/python3
# -*- coding: utf-8 -*-


from collections import deque

# 1.创建deque序列：
d1 = deque()

# 2.deque提供了类似list的操作方法：
d2 = deque()
d2.append(3)
d2.append(8)
d2.append(1)
# 那么此时d2=deque([3,8,1]),len(d)=3,d[0]=3,d[-1]=1

# 3.两端都使用pop:
d3 = deque('12345')
# 那么d3=deque(['1', '2', '3', '4', '5'])
# d3.pop()抛出的是'5',d3.popleft()抛出的是'1'，可见默认pop()抛出的是最后一个元素。

# 4.限制deque的长度
d4 = deque(maxlen=10)
for i in range(20):
    d4.append(str(i))
# 此时d4 = deque(['10', '11', '12', '13', '14', '15', '16', '17', '18', '19'], maxlen=10)
# 可见当限制长度的deque增加超过限制数的项时，另一边的项会自动删除。

# 5.添加list各项到deque中：
d5 = deque([1, 2, 3, 4, 5])
d5.extend([0])
# 此时d5 = deque([1, 2, 3, 4, 5, 0])
d5.extendleft([6, 7, 8])
# 此时d5 = deque([8, 7, 6, 1, 2, 3, 4, 5, 0])
