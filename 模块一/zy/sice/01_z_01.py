# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,
# 然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

# num = 1234
#
# q_num = int(num / 1000) * 1000
#
# b_num = int((int(num / 100) * 100 - q_num ) / 100) * 100
#
# s_num = int((int(num/10) * 10 - q_num  - b_num ) / 10) * 10
#
# g_num = num % 10
# print(int(int((int(num / 100) * 100 - q_num ) / 100)))
# print(int(num / 100) * 100)
# print(int((int(num / 100) * 100 - q_num ) / 100) * 100)
#
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != k) and (i != j) and (j != k):
#                 print(i, j, k)
#
#
# n = "路飞学成"
#
# b = n.encode('utf-8')
# print(b)
#
# print(b.decode("utf-8"))
#
# c= n.encode('gbk')
# print(c)
# print(c.decode("gbk").encode("utf-8").decode("utf-8"))
#
# import copy
# a = [1, 2, 3, ['a', 'b']]
# b = copy.copy(a)
# c = copy.deepcopy(a)
#
# c = ['scs']
# print(a,b,c)

# n = "www.luffycity.com"
#
# n = n.split(".")
#
# print(n)
#
n = "luffycity"
#
# print(n[0:5],"-",n[5:],len(n))
#
# n.replace("city","china")
#
# print(n.replace("city","china"))

# n = ['alex','egon','yuan','wusir','666']
#
# for index,i in enumerate(n):
#     if i == "yuan":
#         print(index)
#         break
#
#
# print(n[-3:])
#
# n = '\\'.join(n)
#
# print(n)

#
# n = [1,3,2,7,6,23,41,24,33,85,56]
#
# for i in range(len(n)-1):
#     for j in range(len(n)-1-i):
#         if n[j] > n[j+1]:
#             n[j], n[j+1] = n[j+1], n[j]
#
#
# print(n)


print(n.ljust(50),n)



























