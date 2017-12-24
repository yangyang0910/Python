# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
'''
角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程 
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校， 
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
6.3 管理视图，创建讲师， 创建班级，创建课程
7. 上面的操作产生的数据都通过pickle序列化保存到文件里
'''
from User import Users
from School import School
from StuClass import StuClass
from Teacher import Teachers
from Students import Students
from Course import Course
def main():
    while True:
        if Users().JudgeLogin():
            role = Users().getRole()
            if role == "root":
                comtent = input("1、创建校区,2、创建班级，3、创建课程，4、查看校区，5、查看班级，6、查看课程 >>> ")
                if comtent == "1":
                    School().CreateSchool()
                elif comtent == "2":
                    StuClass().setClass()
                elif comtent == "3":
                    Course().setCourse()
                elif comtent == "4":
                    StuClass().getReadStuClass()
                elif comtent == "5":
                    StuClass().getReadStuClass()
                elif comtent == "6":
                    Course().getCourseName(Course().getCourse())
                else:
                    print("输入错误，请重新输入")
            elif role == "Teacher":
                comtent = input("1、查看班级学员列表,2、查看课程，3、添加成绩，4、修改成绩 >>> ")
                if comtent == "1":
                    Teachers().CatStudent()
                elif comtent == "2":
                    Teachers().CatCourse()
                elif comtent == "3":
                    Teachers().setAchievement()
                elif comtent == "4":
                    Teachers().midifyAchievement()
                else:
                    print("输入错误，请重新输入")
            elif role == "Student":
                comtent = input("1、购买课程,2、课程查询，3、查看已购买课程, 4、查看成绩 >>> ")
                if comtent == "1":
                    Students().PurchaseCourse()
                elif comtent == "2":
                    Course().getCourseName(Course().getCourse())
                elif comtent == "3":
                    Students().setBuyCourse()
                elif comtent == "4":
                    Students().LookAchievement()
                else:
                    print("输入错误，请重新输入")

if __name__ == "__main__":
    main()







