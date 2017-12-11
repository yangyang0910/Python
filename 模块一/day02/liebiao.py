# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
name = ['adasa','adsaa','asasfa',2,'fasfasfa','fasfasfa','fasfasf',2,'fasfafa','#','!']
#
# print(name[::2])
#
#
# print(name)
#
# name[2] = ['asdsa','ghhhb']
#
# print(name)
#
# name[4:6] = [4,6]
#
# print(name)
#
# name.pop()
#
# print(name)
#
# name.remove(['asdsa','ghhhb'])
#
# print(name)
#
# del name[0]
#
# print(name)
#
# del name[0:2]
#
# print(name)
#
# print("---------------------------")
#
# for i in name:
#     print(i)

# name.sort()

# print(name)
# name.reverse()
# print(name)
#
# count = 0
# for index,i in enumerate(name):
#     print(index,i)


# print(name[name.index(2)+1:].index(2) + name.index(2) + 1)


commodity = [['华为','3999'],['小米','2999'],['苹果','5999'],['魅族','2999'],['天宇','2999'],['OPPE','2999']]
product = []
lethgt = len(commodity)


while True:
    n = input("请选择商品：")

    if not n.isdigit():
        if len(product) == 0:
            print("----------  您未购买任何商品  -----------------")
            b = input("确定要退出吗(y/n)？")
            if b == "y":
                continue
            elif b == "n":
                break
            else:
                print("您输入错误：")
                continue
        else:
            print("----------  您购买的商品有  -----------------")
            for index, i in enumerate(product):
                print(index, "、", i[0], " ", i[1])
            break
    else:
        n = int(n)
        if n >= lethgt and n >= 0:
            print("您输入的有误")
            continue
        else:
            product.append(commodity[n])





