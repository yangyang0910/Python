# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import os
import pickle
from User import Users
from School import School
from StuClass import StuClass
class Teachers(object):
    def __init__(self):
        self.__DB_User = os.path.abspath("../DB/User")
        self.__DB_Teacher = os.path.abspath("../DB/Teacher")
        self.__DB_Course = os.path.abspath("../DB/Course")
        self.__DB_School = os.path.abspath("../DB/School")
        self.__DB_StuClass = os.path.abspath("../DB/StuClass")
        self.__DB_Student = os.path.abspath("../DB/Student")
        self.__DB_Order = os.path.abspath("../DB/Order")
        self.__DB_Achievement = os.path.abspath("../DB/Achievement")

    ''' 查看课程 '''
    def CatCourse(self):
        if Users().JudgeLogin():
            if self.getUser(Users().CookieSession("sessionid")):
                with open(self.__DB_Teacher, "rb") as f:
                    if os.path.getsize(self.__DB_Teacher) == 0:
                        read = {}
                        print("目前没有创建任何课程")
                        return False
                    else:
                        read = pickle.loads(f.read())
                with open(self.__DB_StuClass, "rb") as f:
                    readClass = pickle.loads(f.read())
                    # print(readClass)
                with open(self.__DB_Course, "rb") as f:
                    if os.path.getsize(self.__DB_Course) == 0:
                        reads = {}
                    else:
                        reads = pickle.loads(f.read())
                with open(self.__DB_School, "rb") as f:
                    if os.path.getsize(self.__DB_School) == 0:
                        readschool = {}
                    else:
                        readschool = eval(pickle.loads(f.read()))
                count = True
                for b in reads:
                    for i in read:
                        for a in readClass:
                            if read[i]["stuclass"] == a and reads[b]["class"] == a:
                                for c in readschool:
                                    if readschool[c]["id"] == reads[b]["school"]:
                                        count = False
                                        print("班级：" + readClass[a]["name"], "校区：" + readschool[c]["name"], "开学日期：" + reads[b]["DateofSchool"])
                if count:
                    print("没有创建任何课程")

    ''' 查看班级学生 '''
    def CatStudent(self):
        if Users().JudgeLogin():
            if self.getUser(Users().CookieSession("sessionid")):
                with open(self.__DB_Teacher, "rb") as f:
                    if os.path.getsize(self.__DB_Teacher) == 0:
                        read = {}
                    else:
                        read = pickle.loads(f.read())
                with open(self.__DB_Course, "rb") as f:
                    if os.path.getsize(self.__DB_Student) == 0:
                        Coursereads = {}
                    else:
                        Coursereads = pickle.loads(f.read())
                with open(self.__DB_Order, "rb") as f:
                    if os.path.getsize(self.__DB_Student) == 0:
                        reads = {}
                    else:
                        reads = pickle.loads(f.read())
                count = True
                for i in read:
                    for a in reads:
                        for b in Coursereads:
                            if reads[a]["course"] == b and Coursereads[b]["class"] == read[i]["stuclass"]:
                                count = False
                                print("姓名：" + reads[a]["name"], "班级：" + read[i]["stuclass"])

                if count:
                    print("没有任何学生")

    ''' 过滤老师课程 '''
    def setTeacher(self):
        user = Users().getUser()
        counts = True
        for i in user:
            if user[i]["role"] == "Teacher":
                counts = False
                print("Name:" + i)
        if counts:
            print("没有合适的老师")
            return False
        name = input("Teacher Name:")
        for i in School().ReadSchool():
            print("ID:" + i,"：" + School().ReadSchool()[i]["name"])
        school = input("School ID:").strip()
        schools = StuClass().ReadStuClass()
        count = True
        for i in schools:
            if schools[i]["school"] == school:
                count = False
                print(i)
        if count:
            print("该校区还没符合条件的班级！")
            return False
        stuclass = input("StuClass:").strip()
        if self.FormatTeacher(name, school, stuclass):
            return True
        else:
            return False

    ''' 格式化老师课程 '''
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

    ''' 添加成绩 '''
    def setAchievement(self):
        if Users().JudgeLogin():
            if self.getUser(Users().CookieSession("sessionid")):
                with open(self.__DB_Achievement, "rb") as f:
                    if os.path.getsize(self.__DB_Achievement) == 0:
                        read = {}
                    else:
                        read = pickle.loads(f.read())
                student = input("Student Name>>>:").strip()
                with open(self.__DB_Student, "rb") as f:
                    if os.path.getsize(self.__DB_Student) == 0:
                        reads = {}
                    else:
                        reads = pickle.loads(f.read())
                if student in reads:
                    achievement = input("Achievement>>>:").strip()
                    with open(self.__DB_Teacher, "rb") as f:
                        if os.path.getsize(self.__DB_Teacher) == 0:
                            treads = {}
                        else:
                            treads = pickle.loads(f.read())
                    with open(self.__DB_Course, "rb") as f:
                        if os.path.getsize(self.__DB_Course) == 0:
                            creads = {}
                        else:
                            creads = pickle.loads(f.read())
                    # print(treads)
                    # print(creads)
                    course = ""
                    for a in creads:
                        if treads[Users().CookieSession("sessionid")]["stuclass"] == creads[a]["class"]:
                            course = a
                    data = {"achievement" : achievement, "course" : course}
                    read[student] = data
                    with open(self.__DB_Achievement, "wb") as f:
                        pickle.dump(read,f)
                        print("添加成功", student, "成绩：", achievement)
                        return True
                else:
                    print("学生不存在！")
                    return False

    ''' 修改成绩 '''
    def midifyAchievement(self):
        if Users().JudgeLogin():
            if self.getUser(Users().CookieSession("sessionid")):
                student = input("Student Name>>>:").strip()
                with open(self.__DB_Student, "rb") as f:
                    if os.path.getsize(self.__DB_Student) == 0:
                        read = {}
                    else:
                        read = pickle.loads(f.read())
                if student in read:
                    with open(self.__DB_Achievement, "rb") as f:
                        if os.path.getsize(self.__DB_Achievement) == 0:
                            aread = {}
                        else:
                            aread = pickle.loads(f.read())
                    for i in aread:
                        if i == student:
                            print("目前"+aread[i]["course"]+"学科成绩：", aread[i]["achievement"])
                            course = input("Revised Course>>>:").strip()
                            aread[i]["achievement"] = course
                            break
                    with open(self.__DB_Achievement, "wb") as f:
                        pickle.dump(aread, f)
                        print("修改成功")
                        return True

                else:
                    print("学生分数信息不存在")
                    return False

# print(Teachers().setTeacher())
# Teachers().CatStudent()
# Teachers().CatCourse()
# Teachers().midifyAchievement()


# Teachers().LookAchievement()