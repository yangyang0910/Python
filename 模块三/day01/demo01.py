# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

class Luffy(object):
    school = "郑州科技学院"

    def cla(self):
        print("class")

print(Luffy().__dict__)

Luffy.county = "China"

del Luffy.school

print(Luffy.__dict__)

Luffy.county = "中国"

print(Luffy().__dict__)

print(Luffy.county)





















