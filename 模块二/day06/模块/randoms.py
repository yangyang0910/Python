# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import random

print(random.random())  # 用于生成一个0到1的随机符点数: 0 <= n < 1.0
print(random.randint(1, 2))  # 用于生成一个指定范围内的整数
print(random.randrange(1, 10))  # 从指定范围内，按指定基数递增的集合中获取一个随机数
print(random.uniform(1, 10))  # 用于生成一个指定范围内的随机符点数
print(random.choice('nick'))  # 从序列中获取一个随机元素
li = ['nick', 'jenny', 'car', ]
random.shuffle(li)  # 用于将一个列表中的元素打乱
print(li)
li_new = random.sample(li, 2)  # 从指定序列中随机获取指定长度的片断(从li中随机获取2个元素，作为一个片断返回)
print(li_new)