# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import os
import pickle
from User import Users
from School import School
class StuClass:

    def __init__(self):
        self.__DB_STU = os.path.abspath("../DB/StuClass")
        self.__DB_School = os.path.abspath("../DB/School")

    ''' 过滤创建 '''
    def setClass(self):
        schoolName = School().ReadSchool()
        name = input("Class Name：").strip()
        for i in schoolName:
            print(i, "：" + str(schoolName[i]["name"]))
        school = input("School ID：").strip()
        if self.CreateClass(name, school):
            print(name,"：创建成功！")
        else:
            print("创建失败！")

    ''' 创建班级 '''
    def CreateClass(self, name, school):
        if self.getRole():
            if self.JudgeSchool(school):
                with open(self.__DB_STU, "rb") as f:
                    if os.path.getsize(self.__DB_STU) == 0:
                        read = {}
                    else:
                        read = pickle.loads(f.read())
                data = {"name" : name, "school" : school}
                read[name] = data
                with open(self.__DB_STU, "wb") as f:
                    pickle.dump(read, f)
                    return True

    ''' 修改班级 '''
    def ResiveClass(self):
        pass

    ''' 判断老师是否存在 '''
    def getTeacher(self, teacherid):
        if self.getRole():
            with open(self.__DB_STU, "rb") as f:
                if os.path.getsize(self.__DB_STU) == 0:
                    print("老师不存在！")
                    return False
                else:
                    read = pickle.loads(f.read())

    ''' 判断学校是否存在 '''
    def JudgeSchool(self, school):
        schoolName = School().ReadSchool()
        if school in schoolName:
            return True
        else:
            print("学校不存在")
            return False

    ''' 权限检验 '''
    def getRole(self):
        role = Users().getRole()
        if role == "root" or role == "Teacher":
            return True
        else:
            print("无权操作")
            return False

    ''' 获取班级 '''
    def ReadStuClass(self):
        if os.path.getsize(self.__DB_STU) != 0:
            with open(self.__DB_STU, "rb") as f:
                return pickle.loads(f.read())
    ''' 打印所有班级 '''
    def getReadStuClass(self):
        with open(self.__DB_School, "rb") as f:
            if os.path.getsize(self.__DB_School) == 0:
                read = {}
            else:
                read = eval(pickle.loads(f.read()))
        for i in self.ReadStuClass():
            for a in read:
                if a == self.ReadStuClass()[i]["school"]:
                    print("班级名称：" + i, "，所属校区：" + read[a]["name"])
# StuClass().getTeacher("dc76e9f0c0006e8f919e0c515c66dbba3982f785")
# print(StuClass().JudgeSchool("2ae741a3e8ed090faec3cf75e7d834481c0fca89"))

# print(StuClass().ReadStuClass())
# StuClass().setClass()
# StuClass().getReadStuClass()

