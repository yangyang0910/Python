# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
from Common import Common
import os
class School(object):

    def __init__(self):
        self.__DB_School = os.path.abspath("../DB/School")

    ''' 创建学校 '''
    def CreateSchool(self, name):
        if Common().Write_Withs(self.__DB_School,name):
            print("创建成功")
        else:
            print("创建失败")

    ''' 获取所有的学校 '''
    def ReadSchool(self, add="北京校区"):
        return Common().Read_Withs(self.__DB_School)

    ''' 获取学校 '''
    def getSchoolName(self, schoolid):
        return self.ReadSchool()[schoolid]["name"]

    ''' 课程管理 '''
    def CourseAdministration(self):
        pass

    ''' 判断学校是否存在 '''
    def getSchool(self, schoolid):
        if schoolid in self.ReadSchool():
            return True
        else:
            print("学校不存在！")
            return False

# School().CreateSchool("上海校区")
# print(School().ReadSchool())
# for i in School().ReadSchool():
    # print(i, School().ReadSchool()[i]["name"])

# print(School().getSchoolName("2ae741a3e8ed090faec3cf75e7d834481c0fca89"))
# print(School().getSchool("2ae741a3e8ed090faec3cf75e7d834481c0fca89"))
# print(School().ReadSchool())


