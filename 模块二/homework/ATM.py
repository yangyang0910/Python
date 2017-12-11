# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import os
count = True
dataFiled = ["staff_id","name","age","phone","dept","enroll_date"]
dataFiledL = {"staff_id":0,"name":1,"age":2,"phone":3,"dept":4,"enroll_date":5}
data = []
# 打开文件
def OpenFile(filename,mod="r"):
    try:
        name = "table/" + filename
        f = open(file=name, mode=mod)
        return f
    except Exception as e:
        print(e)
        count = False
        return False
#检测文件
def rOpenFile(filename,mod="r"):
    name = "table/" + filename
    if mod == "r":
        if os.access(name, os.R_OK):
            return True
        else:
            print("No such file or directory:", filename)
            count = False
            return False
    elif mod == "w" or mod == "r+" or mod == "a":
        if os.access(name, os.W_OK):
            return True
        else:
            print("Unreadable table:", filename)
            count = False
            return False
# 判断字段是否存在
def YWfiles(filesdt):
    for g in filesdt:
        if g in dataFiled:
            return True
        else:
            print("字段不存在：", g)
            return False
# where处理
def SWhere(finddata, datas):
    if "where" in finddata:
        finddatas = finddata[-4:]
        if finddatas[2] == ">":
            # select * from staff_table where age > 22
            if int(datas[finddatas[1]]) > int(finddatas[3]):
                return datas
        elif finddatas[2] == "<":
            if int(datas[finddatas[1]]) < int(finddatas[3]):
                return datas
        elif finddatas[2] == "=":
            if str(datas[finddatas[1]]) == str(finddatas[3]):
                return datas
        else:
            if "like" in finddata:
                for index, i in enumerate(finddata):
                    if i == "where":
                        # ['where', 'name', 'like', '"alex', 'li"']
                        newfinddata = finddata[index:]
                        newStr = " ".join(newfinddata[3:])[1:-1]
                        # print(datas[newfinddata[1]].lower())
                        # print(newStr)
                        if newStr in datas[newfinddata[1]].lower():
                            # print(datas[newfinddata[1]])
                            return datas
            else:
                print("无法识别符号：", finddatas[2])
                return False
    else:
        return datas
#SQL 查询数据
def SelectData(finddata):
    if rOpenFile(finddata[3]):
        data = []
        f = OpenFile(finddata[3])
        for i in f:
            i = [a.strip() for a in i.split(",")]
            files = [a.strip() for a in finddata[1].split(",")]
            datas = {}
            for index, s in enumerate(i):
                datas[dataFiled[index]] = s
            if "*" in files:
                filesdts = {}
                da = SWhere(finddata, datas)
                if da == False:
                    return 0
                else:
                    if da != None:
                        data.append(da)
            else:
                filesdt = finddata[1].split(",")
                for g in filesdt:
                    if g in dataFiled:
                        pass
                    else:
                        print("字段不存在：", g)
                        return False
                filesdtts = {}
                for d in filesdt:
                    filesdtts[d] = datas[d]
                da = SWhere(finddata, filesdtts)
                if da == False:
                    return 0
                else:
                    if da != None:
                        data.append(da)
        print(data)
        print("Query Ok！Affected row number：", len(data))
        f.close()
    else:
        print("文件无法打开")
        return False
#SQL 添加数据
# add staff_table Alex Li,25,134435344,IT,2015-10-29
def InsertData(insertdata):
    # alex li, 25, 134435344, it, 2015 - 10 - 29
    StrData = " ".join(insertdata[2:])
    StrDatas = StrData.split(",")

    if len(StrDatas) != 5:
        print("字段数据不够，字段数据个数为：", 5,"您的字段数据个数为：", len(StrDatas))
    else:
        s = rOpenFile(insertdata[1])
        # print(s)
        if s:
            f = OpenFile(insertdata[1],"r")
            num = []
            for k in f:
                try:
                    num.append(int(k.split(",")[0]))
                except Exception as e:
                    pass
                    # print(k.split(",")[0])
                    # print(e)
                    # return 0
            f.close()
            num.sort()
            nums = int(num[-1]) + 1
            StrDatas.insert(0, str(nums))
            count = len(StrDatas)
            StrDatas = ",".join(StrDatas) + "\n"
            g = OpenFile(insertdata[1],"a")
            g.write(StrDatas)
            print("Query Ok！Affected row number：", count)
            g.close()
#SQL 修改数据
# UPDATE staff_table SET dept = "Market" WHERE  dept = "IT"
def UpdataData(updatadata):
    count = 0
    f = OpenFile(updatadata[1], "r+")
    if "where" in updatadata:
        data = []
        for i in f:
            datas = {}
            e = [a.strip() for a in i.split(",")]
            for index, r in enumerate(e):
                datass = updatadata[5].split("\"")
                dataWh = updatadata[-1].split("\"")

                if updatadata[8] == ">":
                    if (dataFiled[index] == updatadata[3]) and (int(e[dataFiledL[updatadata[7]]]) > int(dataWh[0])):
                        count += 1
                        datas[dataFiled[index]] = datass[1]
                    else:
                        datas[dataFiled[index]] = r
                elif updatadata[8] == "<":
                    if dataFiled[index] == updatadata[3] and (int(e[dataFiledL[updatadata[7]]]) < int(dataWh[0])):
                        count += 1
                        datas[dataFiled[index]] = datass[1]
                    else:
                        datas[dataFiled[index]] = r
                elif updatadata[8] == "=":
                    if dataFiled[index] == updatadata[3] and (str(e[dataFiledL[updatadata[7]]]) == str(dataWh[0])):
                        count += 1
                        datas[dataFiled[index]] = datass[1]
                    else:
                        datas[dataFiled[index]] = r
                else:
                    if "like" in updatadata:
                        print("暂不支持like语法")
                        return False
                    else:
                        print("Sorry！语法错误：", updatadata[8])
            data.append(datas)
    else:
        # f = OpenFile(updatadata[1],"r+")
        data = []

        datass = ""
        for i in f:
            datas = {}
            e = [a.strip() for a in i.split(",")]
            for index,r in enumerate(e):
                datass = updatadata[5].split("\"")
                if dataFiled[index] == updatadata[3]:
                    count += 1
                    datas[dataFiled[index]] = datass[1]
                else:
                    datas[dataFiled[index]] = r
            data.append(datas)
        # f.close()
    filedata = []
    for i in data:
        # {'staff_id': '7', 'name': 'Chao Zhang', 'age': '21', 'phone': '13235324334', 'dept': 'Administration','enroll_date': '2011-08-08'}
        filedata.append(list(i.values()))
    filedata = "\n".join([",".join(a) for a in filedata]) + "\n"
    # f = OpenFile(updatadata[1], "w")
    if f.writable():
        f.truncate(0)
        f.write(filedata)
        print("Query Ok！Affected row number：", count)
    else:
        print("Sorry! 文件不可写")
    f.close()
#SQL 删除数据
# del from staff where  id = 3
def DELData(deledet):
    if "where" in deledet:
        if rOpenFile(deledet[2]):
            count = 0
            counts = 0
            data = []
            f = OpenFile(deledet[2], "r+")
            for e in f:
                counts += 1
                e = [a.strip() for a in e.split(",")]
                datas = {}
                for index, s in enumerate(e):
                    datas[dataFiled[index]] = s
                try:
                    if deledet[-2] == ">":
                        # select * from staff_table where age > 22
                        if int(datas[deledet[4]]) <= int(deledet[-1]):
                            data.append(datas)
                        else:
                            count = + 1
                    elif deledet[-2] == "<":
                        if int(datas[deledet[4]]) >= int(deledet[-1]):
                            data.append(datas)
                        else:
                            count = + 1
                    elif deledet[-2] == "=":
                        if int(datas[deledet[4]]) != int(deledet[-1]):
                            data.append(datas)
                        else:
                            count = + 1
                    else:
                        if "like" in deledet:
                            for index, i in enumerate(deledet):
                                if i == "where":
                                    # ['where', 'name', 'like', '"alex', 'li"']
                                    newfinddata = deledet[index:]
                                    newStr = " ".join(newfinddata[3:])[1:-1]
                                    # print(datas[newfinddata[1]].lower())
                                    # print(newStr)
                                    if newStr in datas[newfinddata[1]].lower():
                                        # print(datas[newfinddata[1]])
                                        count += 1
                                    else:
                                        data.append(datas)
                        else:
                            print("无法识别符号：", deledet[5])
                            return False
                except Exception as e:
                    pass
            # f.close()
            filedata = []
            for i in data:
                # {'staff_id': '7', 'name': 'Chao Zhang', 'age': '21', 'phone': '13235324334', 'dept': 'Administration','enroll_date': '2011-08-08'}
                filedata.append(list(i.values()))
            filedata = "\n".join([",".join(a) for a in filedata]) + "\n"
            # f = OpenFile(deledet[2],"w")
            if f.writable():
                f.truncate(0)
                f.write(filedata)
                print("Query Ok! Affected row number：", count, " line")
            else:
                print("Sorry!文件不可写")

        else:
            return 0
        f.close()
    else:
        f = OpenFile(deledet[2], "w+")
        f.truncate(0)
        print("Query Ok, Affected row number：7")
        f.close()
# 处理SQL
def HandleField(sql):
    # select  name, age  from staff_table where  age > 22
    if sql == "":
        return False
    else:
        a = [i.lower() for i in sql.split(" ")]
        while "" in a:
            a.remove("")
        return a
# 解析SQL
def AalysisField(sql):
    # ['select', '*', 'from', 'staff_table']
    sql = HandleField(sql)
    if sql:
        if sql[0] == "select" or sql[0] == "find":
            f = OpenFile(sql[3]).read()
            if count:
                SelectData(sql)
        elif sql[0] == "add":
            InsertData(sql)
        elif sql[0] == "update":
            UpdataData(sql)
        elif sql[0] == "del":
            DELData(sql)
        else:
            if sql[0] == "":
                pass
            else:
                print("SQL语句错误：",sql[0])
    else:
        return False
#启动
while True:
    sql = input("SQL >>>").strip()
    count = True
    if sql == "exit" or sql == "exit()":
        print("Bey!")
        break
    else:
        AalysisField(sql)
















