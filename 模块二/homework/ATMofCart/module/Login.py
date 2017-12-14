# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import json
import os
from Logs import Loggs
from Session import Session
from Cookies import Cookie
class Login(object):

    def __init__(self):
        self.__file_path = os.path.abspath("../DB/DB_table")
        self.__sep = os.path.sep

    ''' 登录 '''
    def login(self, username, password):
        count = False
        with open(self.__file_path +  self.__sep + "user.json", "r") as f:
            # print(f.read())
            s = json.loads(f.read())
            if s[username]["password"] == password:
                count = True
                Loggs().All("登录成功！")
                Session()[username] = username
                return True
            else:
                Loggs().Error("用户不存在或密码错误！")
                return False

    ''' 注销 '''
    def loginout(self,username):
        del Cookie()["sessionid"]
        del Session()[username]
        return True


Login().login("root","root")