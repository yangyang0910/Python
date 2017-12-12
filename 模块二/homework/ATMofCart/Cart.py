# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import http.cookies

from module import Carts

class ages:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.fors(self.name, self.age)

    def fors(self,name,age):
        Carts.Carts().gg()
        # print(name, age)


ages("Alvin", 22)