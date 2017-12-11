# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
import copy
will = ["Will", 28, ["Python", "C#", "JavaScript"]]

wilber = copy.copy(will)
wilberr = copy.deepcopy(will)

print(id(will))
print(id(wilber))
print(id(wilberr))
print("----------------")
print(will)
print(wilber)
print(wilberr)
print("----------------")

will[2][0] = "PHP"

print(id(will))
print(id(wilber))
print(id(wilberr))
print("----------------")
print(will)
print(wilber)
print(wilberr)