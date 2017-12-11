# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import time

print(time.time())     # 返回当前系统时间戳（1970年1月1日0时0分0秒开始）
print(time.ctime()) # 输出Tue May 17 16:07:11 2016，当前系统时间
print(time.ctime(time.time() - 86400)) # 将时间戳转换为字符串格式
print(time.gmtime(time.time() - 86400)) # 将时间戳转换为struct_time格式
print(time.localtime(time.time() - 86400)) # 将时间戳转换为struct_time格式，返回本地时间
print(time.mktime(time.localtime()))  # 与time.localtime()功能相反，将struct_time格式转回成时间戳格式
# time.sleep(5)  　　　　　　　　　　　　　　　　  #sleep停顿
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())) # 将struct_time格式转成指定的字符串格式
print(time.strptime("2016-05-17", "%Y-%m-%d"))  # 将字符串格式转换成struct_time格式


print("----------------------------------------------------------------")
import datetime

print(datetime.date.today())  # 输出格式 2016-05-17
print(datetime.date.fromtimestamp(time.time() - 86400))  # 2016-05-16 将时间戳转成日期格式
current_time = datetime.datetime.now()
print(current_time) # 输出2016-05-17 16:18:28.737561
print(current_time.timetuple())  # 返回struct_time格式
print(current_time.replace(2008, 8, 8)) # 输出2008-08-08 16:21:34.798203,返回当前时间,但指定的值将被替换

str_to_date = datetime.datetime.strptime("28/7/08 11:20", "%d/%m/%y %H:%M")  # 将字符串转换成日期格式
print(str_to_date)
new_date = datetime.datetime.now() + datetime.timedelta(days=10)  # 比现在加10天
new_date = datetime.datetime.now() + datetime.timedelta(days=-10)  # 比现在减10天
new_date = datetime.datetime.now() + datetime.timedelta(hours=-10)  # 比现在减10小时
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120) # 比现在+120s
print(new_date)