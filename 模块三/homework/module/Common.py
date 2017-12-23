# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import time
import pickle
import hashlib
import random
import time
import os
# from Session import Session
# from Cookies import Cookie

class Common:
    def __init__(self, Dates = "%Y-%m-%d %H:%M:%S"):
        self.__Dates = Dates

    ''' 格式化时间 '''
    def Dates(self):
        return time.strftime(self.__Dates, time.localtime())

    ''' 返回当前时间戳 '''
    def Times(self):
        return time.time()

    ''' 读文件 '''
    def Read_Withs(self, filename, mode="rb"):
        with open(filename, mode) as f:
            if os.path.getsize(filename) == 0:
                return False
            else:
                return eval(pickle.loads(f.read()))

    ''' 写文件 '''
    def Write_Withs(self, filename, name, mode="wb"):
        id = self.Jam_hash(str(time.time())+str(random.randint(10000,99999)))
        data = {"id": id ,"name":name}
        read = self.Read_Withs(filename)
        if read:
            read[id] = data
        else:
            read = {id:data}
        with open(filename,mode) as f:
            pickle.dump(str(read), f)
            return True

    ''' 加密 '''
    def Jam_hash(self, password):
        if isinstance(password, str):
            import hashlib
            hs = hashlib.sha1()
            hs.update(bytes(password, encoding="utf-8"))
            return hs.hexdigest()
        else:
            return False

    ''' 解密 '''
    def Jem_hash(self, new=None, old=None):
        new_pasd = self.Jam_hash(new)
        old_pasd = old
        if new_pasd == old_pasd:
            return True
        else:
            return False


# Common().Write_Withs("E:\Python\Python\模块三\homework\DB\School","北京校区")
# obj = Common().Read_Withs("E:\Python\Python\模块三\homework\DB\School")
# print(obj)
