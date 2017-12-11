# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

li = ["alec", "aric", "Alex", "Tony", "rain"]
tu = ("alec", "aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

for i in dic.values():
    # print(i.startswith('a') )
    i = i.strip()
    if (i.startswith('a') or i.startswith('A')) and i.endswith('c'):
        print(i)