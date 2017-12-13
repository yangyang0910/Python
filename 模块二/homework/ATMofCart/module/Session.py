# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import os
import time
import hashlib
import json
# from Cookies import Cookie

class Session(object):
    ''' session '''
    def __init__(self):
        self.__sessionPath = os.path.abspath("../DB/DB_session")
        self.__sessionIDPath = os.path.abspath("../DB/DB_table")
        self.__sep = os.path.sep

    '''制作session的ID'''
    def __createSession(self):
        create_session_id = "%s" % (time.time())
        hash = hashlib.sha1()
        hash.update(bytes(create_session_id , encoding="utf-8"))
        return hash.hexdigest()

    ''' 获取session值 '''
    def __getitem__(self, item):
        with open(self.__sessionIDPath + "\\\\sessionId.json", "r") as f:
            read = f.read()
            if read != "":
                session_id = json.loads(read)
                if item in session_id:
                    session_ids = session_id[item]
                else:
                    return False
            else:
                return False
        count = False
        with open(self.__sessionPath + "\\\\session_" + session_ids + ".json", "r") as f:
            reads = f.read().strip()
            jsonMake = json.loads(reads)
            jsonMakes = jsonMake[session_ids]
            expiryTime = jsonMakes["expiryTime"]
            if jsonMakes["expiry"]:
                Times = time.time() - int(expiryTime)
                mTimes = os.stat(self.__sessionPath + "\\\\session_" + session_ids + ".json").st_mtime
                if int(Times) > int(mTimes):
                    count = True
                else:
                    return jsonMakes["user"]
            else:
                return False

        if count:
            with open(self.__sessionPath + "\\\\session_" + session_ids + ".json", "w") as f:
                jsonMakes["expiry"] = False
                jsonMake[session_ids] = jsonMakes
                json.dump(jsonMake, f)
                return False

    ''' 设置session值 '''
    def __setitem__(self, username, times = 3600):
        session_ID = self.__createSession()
        Session_data = {}
        Session_data[session_ID] = {"user":username,"expiryTime": times, "expiry": True, "createTime": time.time()}
        with open(self.__sessionPath + self.__sep +"session_" + session_ID + ".json", "w") as f:
            json.dump(Session_data,f)
        read = ""
        with open(self.__sessionIDPath + self.__sep + "sessionId.json","r") as f:
            read = f.read()
        with open(self.__sessionIDPath +  self.__sep + "sessionId.json", "w") as f:
            if read is "":
                jsonData = {}
            else:
                jsonData = json.loads(read)
            jsonData[username] = session_ID
            json.dump(jsonData, f)
            return True


    ''' 删除session '''
    def __delitem__(self, user):
        with open(self.__sessionIDPath +  self.__sep + "sessionId.json", "r") as f:
            reads = f.read()
            sessionIds = json.loads(reads)
            if user in sessionIds:
                sessionIds = sessionIds[user]
            else:
                return False
        read = ""
        with open(self.__sessionPath +  self.__sep + "session_" + sessionIds + ".json", "r") as f:
            read = f.read()
        with open(self.__sessionPath +  self.__sep + "session_" + sessionIds + ".json", "w") as f:
            ss = json.loads(read)
            ss[sessionIds]["expiry"] = False
            json.dump(ss, f)
            return True

    ''' 修改过期时间  '''
    def ExpiryTime(self,user,times=3600):
        with open(self.__sessionIDPath +  self.__sep + "sessionId.json", "r") as f:
            reads = f.read()
            sessionIds = json.loads(reads)
            if user in sessionIds:
                sessionIds = sessionIds[user]
            else:
                return False
        read = ""
        with open(self.__sessionPath +  self.__sep + "session_" + sessionIds + ".json", "r") as f:
            read = f.read()
        with open(self.__sessionPath +  self.__sep + "session_" + sessionIds + ".json", "w") as f:
            ss = json.loads(read)
            ss[sessionIds]["expiryTime"] = times
            ss[sessionIds]["expiry"] = True
            json.dump(ss, f)
            return True

