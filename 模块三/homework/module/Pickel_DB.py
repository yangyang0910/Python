# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import pickle
import os
class Pickel_DB:

    def __init__(self):
        self.__Teacher = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(self.__Teacher)

s = Pickel_DB()

print(Pickel_DB.__bases__)





























