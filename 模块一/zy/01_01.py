# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
li = ['alex','eric','rain']

count = ''

for index,i in enumerate(li):
    if len(li) > index + 1:
        count = count + i + "_"
    else:
        count = count + i

print(count)





