# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

while True:
    COUNT = 22
    age = int(input())
    if age == COUNT:
        print("猜对了")
        break
    elif age > COUNT:
        print("大了")
    else:
        print("小了")