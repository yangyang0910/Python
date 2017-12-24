# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import time
import os
import pickle
from Common import Common
from Session import Session
from Cookies import Cookie
from School import School
# from StuClass import StuClass

class Users:
    def __init__(self):
        self.__DB_User = os.path.abspath("../DB/User")
        self.__DB_Teacher = os.path.abspath("../DB/Teacher")
        self.__DB_STU = os.path.abspath("../DB/StuClass")
        self.__DB_Student = os.path.abspath("../DB/Student")

    ''' 登录 '''
    def Login(self):
        username = input("用户名(或注册y or n)>>>:").strip()
        pawd = ""
        if username == "y" or username == "Y":
            self.setRegister()
            self.Login()
        else:
            pawd = input("password>>>:").strip()
        with open(self.__DB_User, "rb") as f:
            if os.path.getsize(self.__DB_User) == 0:
                read = {}
            else:
                read = pickle.loads(f.read())
        if username in read:
            if Common().Jem_hash( pawd,read[username]["password"]):
                session = Session()["username"] = username
                if session:
                    print("登录成功")
                    return True
                else:
                    print("登录失败:A")
                    return False
            else:
                print("登录失败:B")
                return False
        else:
            print("用户不存在")
            return False

    ''' 注册 '''
    def Register(self, username, password, role):
        with open(self.__DB_User, "rb") as f:
            if os.path.getsize(self.__DB_User) == 0:
                read = {}
            else:
                read = pickle.loads(f.read())
        data = {
            "id" : Common().Jam_hash(str(time.time())),
            "username" : username,
            "password" : Common().Jam_hash(password),
            "role" : role
        }
        read[username] = data
        with open(self.__DB_User, "wb") as f:
            pickle.dump(read, f)
            return True

    ''' 过滤注册 '''
    def setRegister(self):
        username = input("UserName>>>:").strip()
        password = input("PassWord>>>:").strip()
        r = ["root", "Teacher", "Student"]
        role = input("Role(root | Teacher | Student)")
        if role in r:
            if self.Register(username, password, role):
                print("注册成功")
                if role == "root":
                    return True
                elif role == "Teacher":
                    self.setTeacher()
                    return True
                elif role == "Student":
                    self.setStudent(username)
                    return True
                else:
                    print("角色输入错误！")
                    return False
            else:
                print("注册失败")
                return False

    ''' 过滤老师课程 '''
    def setTeacher(self):
        user = self.getUser()
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
        schools = self.ReadStuClass()
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

    ''' 获取班级 '''
    def ReadStuClass(self):
        if os.path.getsize(self.__DB_STU) != 0:
            with open(self.__DB_STU, "rb") as f:
                return pickle.loads(f.read())

    ''' 格式化老师课程 '''
    def FormatTeacher(self, name, school, stuclass):
        if self.getTeacherUser(name):
            with open(self.__DB_Teacher, "rb") as f:
                if os.path.getsize(self.__DB_Teacher) == 0:
                    read = {}
                else:
                    read = pickle.loads(f.read())
            data = {"username": name, "school": school, "stuclass": stuclass, }
            read[name] = data
            with open(self.__DB_Teacher, "wb") as f:
                pickle.dump(read, f)
                return True

    ''' 判断用户是否存在 '''
    def getTeacherUser(self, name):
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

    ''' 通过cookie获取用户名 '''
    def CookieSession(self, cookieId):
        cookieid = Cookie()[cookieId]
        if cookieid:
            return Session()[cookieid]
        else:
            return False

    ''' 获取用户角色 '''
    def getRole(self):
        if self.JudgeLogin():
            user = self.CookieSession("sessionid")
            if user:
                with open(self.__DB_User, "rb") as f:
                    read = pickle.loads(f.read())
                    return read[user]["role"]

    ''' 判断用户是否登录 '''
    def JudgeLogin(self):
        user = self.CookieSession("sessionid")
        if not user:
            if self.Login():
                return True
            else:
                return False
        else:
            return True



# Users().Login()
# print(Users().CookieSession("sessionid"))
# Users().Register("Mosson", "root", "Teacher")
# print(Users().getRole())

    ''' 获取USER '''
    def getUser(self):
        with open(self.__DB_User, "rb") as f:
            if os.path.getsize(self.__DB_User) != 0:
                return pickle.loads(f.read())
            else:
                return False

    ''' 过滤创建学员 '''
    def setStudent(self, name):
        # name = input("Student Name>>>:").strip()
        if self.getStudentUser(name):
            for i in School().ReadSchool():
                print("ID:" + i, "：" + School().ReadSchool()[i]["name"])
            school = input("School ID:").strip()
            if not School().getSchool(school):
                return False
            count = True
            schools = self.ReadStuClass()
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
        if self.getStudentUser(name):
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
    def getStudentUser(self, name):
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
