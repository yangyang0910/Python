# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import shutil

# 将文件内容拷贝到另一个文件中
# shutil.copyfileobj(open("old.json",'r'),open("new.json",'w'))

# 拷贝文件
# shutil.copyfile("old.json","new.json")

# 仅拷贝权限
# shutil.copymode("old.json","new.json")

# shutil.copystat("old.json","new.json")

#创建压缩包并返回文件路径，例如：zip、tar
# print(shutil.make_archive("new.json","zip",root_dir="E:\Python\模块二\day06\模块"))
w = shutil.make_archive("E:\Python\模块二\day06\\new","zip",root_dir="E:\Python\模块二\day06\模块")
print(w)
#解压
import zipfile
z = zipfile.ZipFile(w, "r")
z.extractall()
z.close()
# z.write("new.json")
# z.close()








