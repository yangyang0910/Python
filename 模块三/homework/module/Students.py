# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import os
import pickle
import time
import random
from School import School
from StuClass import StuClass
from User import Users
from Common import Common
class Students(object):
    def __init__(self):
        self.__DB_User = os.path.abspath("../DB/User")
        self.__DB_Student = os.path.abspath("../DB/Student")
        self.__DB_Course = os.path.abspath("../DB/Course")
        self.__DB_School = os.path.abspath("../DB/School")
        self.__DB_Order = os.path.abspath("../DB/Order")

    ''' 购买课程 '''
    def PurchaseCourse(self):
        if Users().JudgeLogin():
            if self.getUser(Users().CookieSession("sessionid")):
                with open(self.__DB_Order, "rb") as f:
                    if os.path.getsize(self.__DB_Order) == 0:
                        read = {}
                    else:
                        read = pickle.loads(f.read())
                self.getCourse()
                with open(self.__DB_Course, "rb") as f:
                    if os.path.getsize(self.__DB_Course) == 0:
                        reads = {}
                    else:
                        reads = pickle.loads(f.read())
                course = input("Course Name>>>").strip()
                if course in reads:
                    price = reads[course]["price"]
                else:
                    print("课程不存在")
                    return False
                data = {"name":Users().CookieSession("sessionid"), "course" : course, "price":price,"createTime":time.time()}
                read[Common().Jam_hash(str(time.time())+str(random.randint(10000,99999)))] = data
                with open(self.__DB_Order, "wb") as f:
                    pickle.dump(read, f)
                    print("购买成功！")
                    return True

    ''' 课程查询 '''
    def getCourse(self):
        with open(self.__DB_Course, "rb") as f:
            if os.path.getsize(self.__DB_Course) == 0:
                read = {}
            else:
                read = pickle.loads(f.read())
        with open(self.__DB_School, "rb") as f:
            if os.path.getsize(self.__DB_Student) == 0:
                reads = {}
            else:
                reads = eval(pickle.loads(f.read()))
        for i in read:
            for a in reads:
                if reads[a]["id"] == read[i]["school"]:
                    print("课程名称："+i, "价格：" + read[i]["price"], "校区：" + reads[a]["name"], "开学日期：" + read[i]["DateofSchool"])

    ''' 获取学员余额 '''
    def getMoney(self):
        if Users().JudgeLogin():
            if self.getUser(Users().CookieSession("sessionid")):
                with open(self.__DB_Student, "rb") as f:
                    if os.path.getsize(self.__DB_Student) == 0:
                        return False
                    else:
                        read = pickle.loads(f.read())
                        return read[Users().CookieSession("sessionid")]["money"]

    ''' 过滤创建学员 '''
    def setStudent(self, name):
        if self.getUser(name):
            for i in School().ReadSchool():
                print("ID:" + i, "：" + School().ReadSchool()[i]["name"])
            school = input("School ID:").strip()
            if not School().getSchool(school):
                return False
            count = True
            schools = StuClass().ReadStuClass()
            for i in schools:
                if schools[i]["school"] == school:
                    count = False
                    print(i)
            if count:
                print("该校区还没符合条件的班级！")
                return False
            stuclass = input("StuClass:").strip()
            if self.CreateStudent(name, school, stuclass):
                return True
            else:
                return False

    ''' 创建学员 '''
    def CreateStudent(self, name, school, stuclass):
        if self.getUser(name):
            with open(self.__DB_Student, "rb") as f:
                if os.path.getsize(self.__DB_Student) == 0:
                    read = {}
                else:
                    read = pickle.loads(f.read())

                data = {"name":name, "school":school, "stuclass":stuclass, "money" : 10000}
                read[name] = data
                with open(self.__DB_Student, "wb") as f:
                    pickle.dump(read, f)
                    return True

    ''' 判断用户是否存在 '''
    def getUser(self, name):
        if os.path.getsize(self.__DB_User) != 0:
            with open(self.__DB_User, "rb") as f:
                read = pickle.loads(f.read())
                if name in read:
                    if read[name]["role"] == "Student":
                        return True
                    else:
                        print("角色不正确")
                        return False
                else:
                    print("学员名称不存在")
                    return False


# Students().setStudent("Alvin")
# print(Students().getMoney())
Students().PurchaseCourse()