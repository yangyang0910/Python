# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import os
from Tshash import Tshash
from Session import Session
import json
class User(object):
    ''' 用户管理 '''

    def __init__(self):
        # E:\Python\Python\模块二\homework\ATMofCart\DB_table
        self.__DbPath = os.path.abspath("../DB/DB_table/")

    ''' 添加用户 '''
    def AddUser(self, username, password=None):
        pass

    ''' 删除用户 '''
    def DelUser(self, user):
        pass

    ''' 软删除用户 '''
    def ReUser(self,user):
        pass

    ''' 冻结用户 '''
    def FrozenUser(self, user):
        pass

    ''' 修改用户权限 '''
    def JurisdictionUser(self):
        pass

    ''' 用户登录状态操作 '''
    def LoginUser(self,user):
        pass

    ''' 获取用户权限 '''
    def AccesstoJurisdictionUser(self,user):
        # jurisdiction
        with open(self.__DbPath + "\\user.json", 'r') as f:
            return json.loads(f.read())[user]["jurisdiction"]




