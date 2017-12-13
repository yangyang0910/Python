# -*- coding:utf-8 -*-
# AUTHER   @ Alvin


class A(object):
    def __init__(self,name):
        self.name = name
        self.aa()

    def aa(self):
        print(self.name)


class B(A):

    def __init__(self, name):
        self.name = name
        super(B,self).__init__(self.name)
        self.bb()


    def bb(self):
        print(self.name)

class C(B):

    def __init__(self, name):
        self.name = name
        super(C,self).__init__(self.name)
        self.bb()


    def bb(self):
        print(self.name)


class D(C):

    def __init__(self, name):
        self.name = name
        super(D,self).__init__(self.name)
        self.bb()


    def bb(self):
        print(self.name)



D("Alvin")









