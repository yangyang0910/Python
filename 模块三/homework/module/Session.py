# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import os
import time
import hashlib
import pickle
from Cookies import Cookie

class Session:
    ''' session '''
    def __init__(self):
        self.__sessionPath = os.path.abspath("../DB/DB_session")
        self.__sessionIDPath = os.path.abspath("../DB")
        self.__sep = os.path.sep

    '''制作session的ID'''
    def __createSession(self):
        create_session_id = "%s" % (time.time())
        hash = hashlib.sha1()
        hash.update(bytes(create_session_id , encoding="utf-8"))
        return hash.hexdigest()

    ''' 获取session值 '''
    def __getitem__(self, item):
        sessionPath = self.__sessionPath + self.__sep + "session_" + item
        if os.path.exists(sessionPath):
            with open(sessionPath, "rb") as f:
                read = pickle.loads(f.read())
                if read["id"] == item:
                    return read["username"]
                else:
                    return False

    ''' 设置session值 '''
    def __setitem__(self, key, value):
        sessionId = self.__createSession()
        data = {"id":sessionId, key:value}
        with open(self.__sessionPath+self.__sep+"session_"+sessionId, "wb") as f:
            pickle.dump(data, f)
            Cookie()["sessionId"] = sessionId
            return True

    ''' 删除session '''
    def __delitem__(self, key):
        os.remove(self.__sessionPath+self.__sep+"session_"+key)

# print(Session().CookieSession("sessionid"))
# Session()["username"] = "root"
# print(Session()["28718cf666a23afc979ce720b89b449087025a71"])





