# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

n = "Hello Word"
# print(n.swapcase()) # 大写变小写，小写变大写
#
# print(n.capitalize()) # 首字母变大些
#
# print(n.casefold()) # 全变小写
#
# print(n.count("o")) # 统计某字母数量
#
# print(n.endswith("d")) # 统计受否以某字符串结尾
#
# print(n.startswith('H')) # 统计是否是某字符串开头
#
# print(n.islower()) # 判断是否全是小写
#
# print(n.lower()) # 全部变小写
#
# print(n.upper()) # 全部变大写
#
# s = "\n Hello World"
#
# print(s)
#
# print(s.strip())  # 清除特殊字符
#
#
# str_in = "qwertyuiopasdfghjklzxcvbnm"
# str_out = "!@#$%^&*()_+.,';:?`~。，‘“；："
#
# table = str.maketrans(str_in,str_out)
#
# print(table)
#
a = "HHHlo World"

# print(a.translate(table))AHH


# 字符串替换

try:
    print(a.replace("H", "A", 2))
except (Exception) as e:
    print(e)


