# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import time
import os
import pickle
from Common import Common
from Session import Session
from Cookies import Cookie

class Users:
    def __init__(self):
        self.__DB_User = os.path.abspath("../DB/User")

    ''' 登录 '''
    def Login(self):
        username = input("username>>>:").strip()
        pawd = input("password>>>:").strip()
        with open(self.__DB_User, "rb") as f:
            if os.path.getsize(self.__DB_User) == 0:
                read = {}
            else:
                read = pickle.loads(f.read())
        if username in read:
            if Common().Jem_hash( pawd,read[username]["password"]):
                session = Session()["username"] = username
                if session:
                    print("登录成功")
                    return True
                else:
                    print("登录失败:A")
                    return False
            else:
                print("登录失败:B")
                return False
        else:
            print("用户不存在")
            return False

    ''' 注册 '''
    def Register(self, username, password, role):
        with open(self.__DB_User, "rb") as f:
            if os.path.getsize(self.__DB_User) == 0:
                read = {}
            else:
                read = pickle.loads(f.read())
        data = {
            "id" : Common().Jam_hash(str(time.time())),
            "username" : username,
            "password" : Common().Jam_hash(password),
            "role" : role
        }
        read[username] = data
        with open(self.__DB_User, "wb") as f:
            pickle.dump(read, f)
            return True

    ''' 通过cookie获取用户名 '''
    def CookieSession(self, cookieId):
        cookieid = Cookie()[cookieId]
        if cookieid:
            return Session()[cookieid]
        else:
            return False

    ''' 获取用户角色 '''
    def getRole(self):
        if self.JudgeLogin():
            user = self.CookieSession("sessionid")
            if user:
                with open(self.__DB_User, "rb") as f:
                    read = pickle.loads(f.read())
                    return read[user]["role"]

    ''' 判断用户是否登录 '''
    def JudgeLogin(self):
        user = self.CookieSession("sessionid")
        if not user:
            if self.Login():
                return True
            else:
                return False
        else:
            return True



# Users().Login()
# print(Users().CookieSession("sessionid"))
# Users().Register("Mosson", "root", "Teacher")
# print(Users().getRole())