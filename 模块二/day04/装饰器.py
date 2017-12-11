# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

def outer(func):
    def inner():
        print("123")
        r = func()
        print("456")
        return r
    return inner

@outer
def index():
    print(1)
    return 11

index()





