# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import os
import pickle
import time
from Common import Common

class Cookie(object):
    ''' Cookie操作 '''
    def __init__(self):
        ''' 获取系统类型 '''
        self.__GenreSystem = os.name
        self.__CreateFolder()
        self.__sep = os.path.sep

    ''' 判断需要的文件夹是否存在 '''
    def __DwFolder(self, path):
        if os.path.isdir(path):
            return True
        else:
            return False

    ''' cookieID制作 '''
    def __MakeCookie(self, key):
        return Common().Jam_hash("cookie_" + key)

    ''' 创建文件夹 '''
    def __CreateFolder(self):
        if self.__GenreSystem == "nt":
            paths = "C:\\.cookie"
            if not self.__DwFolder(paths):
                try:
                    os.makedirs(paths)
                    return True
                except Exception as e:
                    return False
            return True
        elif self.__GenreSystem == "posix":
            paths = "/User/cookiess"
            if not self.__DwFolder(paths):
                try:
                    os.makedirs(paths)
                    return True
                except Exception as e:
                    return False
        else:
            return False

    ''' 获取当前系统Cookie文件夹路径 '''
    def __DwCookiePath(self):
        Wpaths = "C:\\.cookie"
        Mpaths = "/User/cookiess"
        if self.__GenreSystem == "nt" and self.__DwFolder(Wpaths):
            return Wpaths
        elif self.__GenreSystem == "posix" and not self.__DwFolder(Mpaths):
            return Mpaths
        else:
            return False

    ''' 获取当前系统Cookie路径 '''
    def __DwCookiefilePath(self):
        paths = self.__DwCookiePath()
        if paths:
            if self.__GenreSystem == "nt":
                if not os.path.exists(paths + "\cookie.json"):
                    with open(paths + "\cookie.json", "w") as f:
                        pass
                return paths + "\cookie.json"
            else:
                return paths + "/cookie.json"
        else:
            return False


    ''' 获取Cookie '''
    def __getitem__(self, item):
        if os.path.exists(self.__DwCookiefilePath()):
            paths = self.__DwCookiePath()
            with open(paths+self.__sep+"cookie.json", "rb") as f:
                read = pickle.loads(f.read())
                if item in read:

                    return read[item]
                else:
                    return False
        else:
            return False

    ''' 创建Cookie '''
    def __setitem__(self, key, value):
        if os.path.exists(self.__DwCookiefilePath()):
            paths = self.__DwCookiePath()
            data = {"cookie":self.__MakeCookie(key), "sessionid" : value}
            with open(paths+self.__sep+"cookie.json", "wb") as f:
                pickle.dump(data, f)
                return True
        else:
            return False

    ''' 删除Cookie '''
    def __delitem__(self, key):
        paths = self.__DwCookiePath()
        os.remove(paths+self.__sep+"cookie.json")

# print(Cookie()["sessionid"])




