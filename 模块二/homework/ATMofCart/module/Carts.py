# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
from Tshash import Tshash
class Cart(object):
    def __init__(self):
        pass
    __instanced = None

    ''' 添加购物车 '''
    def AddCart(self):
        pass

    ''' 清空购物车 '''
    def DelCartAll(self):
        pass

    ''' 删除一个商品 '''
    def DelCartOnce(self, goods_id):
        pass

    ''' 修改购物车商品信息 '''
    def ModifyCart(self):
        pass

    ''' 获取当前用户信息 '''
    def __ObtainUser(self):
        pass

    ''' 返回购物车信息 '''
    def ObtainResult(self):
        pass

    ''' 测试 '''
    def ce(self):
        print("SSS")

    ''' 获取Cart对象 '''
    @staticmethod
    def ObtainInstanced():
        if Cart.__instanced:
            return Cart.__instanced
        else:
            Cart.__instanced = Cart()
            return Cart.__instanced


Cart.ObtainInstanced().ce()