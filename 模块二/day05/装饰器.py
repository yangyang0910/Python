# -*- coding:utf-8 -*-
# AUTHER   @ Alvin




def outer2(func2):
    def inner2(*args, **kwargs):
        print('开始')
        r = func2(*args, **kwargs)
        print('结束')
        return r

    return inner2


def outer1(func1):
    def inner1(*args, **kwargs):
        print('start')
        r = func1(*args, **kwargs)
        print('end')
        return r

    return inner1


@outer2  # 这里相当于执行了 f=outer1(f)  f=outer2(f)，步骤如下
@outer1  # 1、f=outer1(f) f被重新赋值为outer1(1)的返回值inner1，
def f():  # 此时func1为 f():print('f 函数')
    print('f 函数')  # 2、f=outer2(f) 类似f=outer2(inner1) f被重新赋值为outer2的返回值inner2
    #    此时func2 为inner1函数 inner1里面func1函数为原来的 f():print('f 函数')


f()
