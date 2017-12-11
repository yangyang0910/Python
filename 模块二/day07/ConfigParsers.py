# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import configparser

con = configparser.ConfigParser()
con.read("my.ini", encoding="utf-8")

result = con.sections()
print(result)