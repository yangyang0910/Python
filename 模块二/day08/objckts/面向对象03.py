# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
class Province:

    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')

# 获取类的成员，即：静态字段、方法、
print(Province.__dict__)
# 输出：{'country': 'China', '__module__': '__main__', 'func': <function func at 0x10be30f50>, '__init__': <function __init__ at 0x10be30ed8>, '__doc__': None}

obj1 = Province('shangxi',10000)
print(obj1.__dict__)
# 获取 对象obj1 的成员
# 输出：{'count': 10000, 'name': 'shangxi'}

obj2 = Province('shangdong', 3888)
print(obj2.__dict__)
# 获取 对象obj1 的成员
# 输出：{'count': 3888, 'name': 'shangdong'}

