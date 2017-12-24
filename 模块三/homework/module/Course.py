# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import os
import pickle
from User import Users
from School import School
from StuClass import StuClass
class Course(object):
    def __init__(self):
        self.__DB_Course = os.path.abspath("../DB/Course")

    ''' 格式化课程 '''
    def setCourse(self):
        name = input("Course Name:").strip()
        DateofSchool = input("Date of School:").strip()
        cycle = input("Cycle:").strip()
        price = input("Price:").strip()
        for i in School().ReadSchool():
            print("ID:" + i,"：" + School().ReadSchool()[i]["name"])
        school = input("School ID:").strip()
        if not School().getSchool(school):
            print("DDD")
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
        if self.CreateCourse(name, DateofSchool, cycle, price, school, stuclass):
            print("创建成功！")
            return True
        else:
            print("创建失败！")
            return False

    ''' 创建课程 '''
    def CreateCourse(self, name,DateofSchool, cycle, price, school, stuclass):
        if School().getSchool(school):
            if self.getRole():
                with open(self.__DB_Course, "rb") as f:
                    if os.path.getsize(self.__DB_Course) == 0:
                        read = {}
                    else:
                        read = pickle.loads(f.read())
                data = {"DateofSchool":DateofSchool, "cycle":cycle, "price":price, "school" : school, "class": stuclass}
                read[name] = data
                with open(self.__DB_Course, "wb") as f:
                    pickle.dump(read, f)
                    return True

    ''' 获取课程 '''
    def getCourse(self):
        # if self.getRole():
        with open(self.__DB_Course, "rb") as f:
            return pickle.loads(f.read())

    ''' 格式化课程 '''
    def getCourseName(self, read):
        for i in read:
            print(str(i + "：").center(20, "*"))
            print("开学日期：", str(read[i]["DateofSchool"]))
            print("学习周期：", str(read[i]["cycle"]) + " month")
            print("购买价格：", "￥ " + str(read[i]["price"]))
            print("开课学校：", str(School().getSchoolName(read[i]["school"])))

    ''' 删除课程 '''
    def DelCourse(self):
        if self.getRole():
            pass

    ''' 权限检验 '''
    def getRole(self):
        role = Users().getRole()
        if role == "Teacher" or role == "root":
            return True
        else:
            print("无权操作")
            return False


# print(Course().getCourse())
# Course().setCourse()
# print(Course().CreateCourse("go", "2018-05-09", 5.5, 8999.00, "81196aeebb12298bdefd9da491d9626b70ca6e60"))
