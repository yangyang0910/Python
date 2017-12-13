# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

class A(object):
    '''
    This is wangbadan
    '''
    name = "AA"
    __name = "ASS"
    def __init__(self):
        pass
        # print(self.__name)
        # print(self.__module__)
        # print(self.__class__)

    @staticmethod
    def aa():
        print("AA")

    @classmethod
    def bb(cls):
        print("BB")

    def __del__(self):
        print("SSS")

    def __call__(self, *args, **kwargs):
        print(args)
        print("call")
        print(self.__dict__)

    def __str__(self):

        return "就不让你打印"
# A().aa()
#
# A().bb()
#
# print(A().name)
#
# print(A().__doc__)

print(A())

























