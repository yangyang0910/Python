# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import json
from Logs import Loggs
class Login(object):

    def __init__(self):
        import os
        self.__file_path = os.path.abspath("../DB/DB_table")

    def login(self, username, password):
        with open(self.__file_path + "/User.json", "r") as f:
            s = json.loads(f.read())
            try:
                name = s[username]
                Loggs().All("登录成功！")
                return True
            except Exception as a:
                Loggs().Error(str(a) + "用户不存在或密码错误！")
                return False

    def loginout(self):
        pass
