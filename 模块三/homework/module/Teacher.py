# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import os
import pickle
class Teachers(object):
    def __init__(self):
        self.__DB_User = os.path.abspath("../DB/User")
        self.__DB_Teacher = os.path.abspath("../DB/Teacher")

    ''' 查看课程 '''
    ''' 查看班级学生 '''
    ''' 格式化老师 '''
    def FormatTeacher(self, name, school, stuclass):
        if self.getUser(name):
            with open(self.__DB_Teacher, "rb") as f:
                if os.path.getsize(self.__DB_Teacher) == 0:
                    read = {}
                else:
                    read = pickle.loads(f.read())
            data = {"username" : name, "school" : school,"stuclass" : stuclass,}
            read[name] = data
            with open(self.__DB_Teacher, "wb") as f:
                pickle.dump(read, f)
                return True

    ''' 判断用户是否存在 '''
    def getUser(self, name):
        if os.path.getsize(self.__DB_User) != 0:
            with open(self.__DB_User, "rb") as f:
                read = pickle.loads(f.read())
                if name in read:
                    if read[name]["role"] == "Teacher":
                        return True
                    else:
                        print("角色不正确")
                        return False
                else:
                    print("教师名称不存在")
                    return False

# print(Teachers().getUser("Mosson"))