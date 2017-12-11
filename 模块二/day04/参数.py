# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

# def aa(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# aa("a","b","c","d",kwargs="dasd")

# a = [i+1 for i in range(10)]
#
# print(a)

# a = [i if i % 2 == 0 else None for i in range(101)]
#
# print(a)


# a = (i for i in range(12))
#
# # for i in range(11):
# #     print(next(a))
# print([next(a) for i in a])
def rr(c):
    print(c)
def range2(n):
    count = 0
    while count < n:
        count += 0.1
        x = yield count
        yield x
        # print(y)

# for i in range2(1):
#     print(i)
f = range2(1)
for i in f:
    print(i)
    print(f.send(5))

# print(f.send(1))
