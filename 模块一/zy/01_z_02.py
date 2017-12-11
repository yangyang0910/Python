# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import json
# 基础需求：
# 让用户输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后退出程序
#
# 升级需求：
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）

# 商品列表
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

# 用户列表
user = {"root":"root","admin":"admin"}

goods_cart = {}
cart = {}
cart['wage'] = 0
cart['goods'] = []
cart['consumption'] = 0
cart['balance'] = 0
status = 0
user_status = {}
with open("01_z_02","r+") as f:
    r = f.read()
    if r == "":
        user_status['status'] = 0
    else:
        user_status = eval(r)
# 工资更新
def wages(wages):
    cart['wage'] = wages
    cart['balance'] = goods_cart['wage'] - goods_cart['consumption']
# 购物车打印
def prints(carts):
    print("购买商品清单".center(30, '-'))
    print("工资：%d" % (carts['wage']))
    print("商品：".center(20, "-"))
    if len(carts['goods']) == 0:
        print("无")
    else:
        for s in carts['goods']:
            print("名称：%s  单价：%s" % (s['name'], s['price']))
    print("消费金额：%s" % (carts['consumption']))
    print("余额：%s" % (carts['balance']))

while True:
    username = input("用户名：")
    password = input("密码：")
    goods_cart = cart
    if int(user_status['status']) < 3:
        if username in user.keys() and user[username] == password:
            if cart['wage'] == 0:
                wage = int(input("工资："))
                wages(wage)
            else:
                ifs = input("是否更新工资(y/n)")
                if ifs == "y":
                    wage = int(input("工资："))
                    wages(wage)
            while True:
                good = input("商品(a查询，q退出)")
                status = 0
                if good == "q":
                    cart = goods_cart
                    prints(goods_cart)
                    break
                elif good == "a":
                    prints(goods_cart)
                else:
                    for i in goods:
                        if good == i["name"]:
                            if goods_cart['balance'] >= i['price']:
                                goods_cart['consumption'] = goods_cart['consumption'] + i['price']
                                goods_cart['balance'] = goods_cart['wage'] - goods_cart['consumption']
                                goods_cart['goods'].append(i)
                                status = 1
                            else:
                                print("余额不够")
                    if status == 0:
                        print("商品不存在")
        else:
            user_status['status'] += 1
            print("用户名或密码错误！")
    elif user_status['status'] >= 3:
        with open("01_z_02", "w+") as f:
            f.write(json.dumps(user_status))
        print("密码错误次数过多")

