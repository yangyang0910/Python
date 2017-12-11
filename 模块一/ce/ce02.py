# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

# ①
# count = 0
#
# for i in range(101):
#     count = count + i
#
# print(count)
#
# ②
# num = input("请输入>>>")
#
# num = int(num)
#
# if num % 4 == 0 and num % 100 != 0:
#     print("YES")
# elif num % 400 == 0:
#     print("NO")
# ③
# n = "www.luffycity.com"
#
# a = n.split('.')
#
# b  = '-'.join(a)
#
# print(b)
#

# n = "www.luffycity.com"

# print(n[0:4])


# print(len(n))

n = ['alex','egon','yuan','wusir','666']

# print(n.index("alex"))

# print(len(n))

# n[0] = "背锅侠"
#
# print(n)

# n.append("a")
#
# print(n)

s = {"Development":"开发小哥","OP":"运维小哥","Operate":"运营小仙女","UI":"UI小仙女"}

# print(s["OP"])

# s["OP"] = "背锅侠"
#
# print(s)

# s["a"] = "b"
#
# print(s)


#求100以内不能被3整除的所有数，并把这些数字放在列表sum=[]里，并求出这些数字的总和和平均数。
sum = []
count = 0
counts = 0
for i in range(101):
    if i % 3 != 0:
        sum.append(i)

for i in sum:
    counts = i + counts

print("和：%d" % (counts))
print("平均数:%d" % (counts / len(sum)))

















