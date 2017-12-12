# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import re

f = open("re",'r')

data = f.read()

print(re.findall('1[0-9]{10}', data))


data = "127.198.12.a2a"

print(re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", data))
