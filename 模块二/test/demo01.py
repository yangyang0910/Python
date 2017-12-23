# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
read = []
with open("02第二模块之三体语录", "r", encoding="utf-8") as f:
    read = f.readlines()
    read[-1] = "给时光以生命，而不是给生命以时光"

with open(r"02第二模块之三体语录", "w", encoding="utf-8") as f:
    f.write(str(read))
#     a = ""
#     for i in read:
#         a += i
#     f.write(a)
        # print(res)
        # read = str(read)
        # print(read)
        # print(read)
        #
        # read = f.readlines()
        # print(read)
        # for i in read:
        #     count += 1
        #         read[4] = read[4][:-1] + "给岁月以文明，而不是给文明以岁月"
        #     if count == 4:
        # read = f.readlines()
        # count = 0
        # print(f.read(2))
        # f.seek(15)
        # print(f.read())
    # print(f.read(2))
    # f.seek(15)
    #     count += 1
    #         print(i.replace("不要回答", "绝对不能回复"))
    #     if count == 2:
    # for i in f.readlines():
    # count = 0
#     read = f.readline()
#     print(type(read), read)

import time
def ll(func):
    def inner(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        long = time.time()-start
        print(long)
        return r
    return inner()


@ll
def aa():
    time.sleep(2)











