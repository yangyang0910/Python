# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import chardet
# ①
# f = open(file="./模特",mode='r', encoding='utf-8')
#
# data = f.read()
#
# print(data)
#
# f.close()

# ②

# f = open(file="./模特",mode='rb')
#
# data = f.read()
#
# f.close()

result = chardet.detect(open(file="./模特",mode='rb').read())

# print(type(result['encoding']))

encodings = result['encoding']

# print(encodings)

f = open(file="./模特",mode='r',encoding = encodings)

# datas = f.read()

for i in f:
    print(i)
# print(f)

f.close()
f = open(file="./模特",mode='w',encoding = encodings)

f.write("模特 is very 漂亮b")

f.close()

f = open(file="./模特",mode='a',encoding = encodings)

f.write("\n模特 is very 漂亮c")

f.close()