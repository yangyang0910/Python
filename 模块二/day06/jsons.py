# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

# import json
# import pickle

# data = {
#     "A":"b",
#     "As":["A","B","C"]
# }

# print(type(json.dumps(data)),json.dumps(data))
# f = open("new.json", "wb")
# pickle.dump(data,f)

# f = open("new.json","rb")
# pickle.loads()


# d = json.dumps(data)
#
# print(json.loads(d))

##### json.loads 将字符串转换为python基本数据类型 列表字典 #####
import json
#
# l = '["nick","jenny","car"]'
# print(l, type(l))
# l = json.loads(l)
# print(l, type(l))
#
# l = '{"k1":"nick","k2:":"jenny"}'
# print(l, type(l))
# l = json.loads(l)
# print(l, type(l))
#
# ##### json.dumps 将python的数据类型列表字典转换为字符串 ######
# # import json
#
# l = ["nick", "jenny", "car"]
# print(l, type(l))
# l = json.dumps(l)
# print(l, type(l))
#
# l = {"k1": "nick", "k2:": "jenny"}
# print(l, type(l))
# l = json.dumps(l)
# print(l, type(l))

##### json dump、load 文件相关 #####
# import json
#
# l = {"k1": "nick", "k2:": "jenny","k3:": "jenny"}
#
# with open('old.json', 'w') as f:
#     json.dump(l,f)
#
# ret = json.load(open('old.json'))
# print(ret)