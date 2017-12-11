li = ['alex','eric','rain','Alvin','Jack','Moss','Mott','Mullen']
#	计算列表长度并输出
print(len(li))
# 	列表中追加元素“seven”，并输出添加后的元素
li.append("seven")
print(li[len(li)-1])
# 	请修改列表第二个位置的元素为“Kelly”，并输出修改后的列表
li.insert(1,"Kelly")
print(li)
# 	请删除列表中元素“Eric”,并输出修改后的列表
li.remove("eric")
print(li)
# 	请删除列表中第二个元素，并输出删除的元素的值和删除元素后的列表
print(li.pop(1))
print(li)
# 	请删除列表中第三个元素，并输出删除元素后的列表
del li[2]
print(li)
# 	请删除列表中第二至四的元素，并输出删除元素后的列表
del li[1:4]
print(li)
# 	请将列表所有的元素反转，并输出反转后的列表
li.reverse()
print(li)
# 	请使用for\len\range输出列表索引
for index,i in enumerate(range(len(li))):
    print(index)
# 	请使用enumrate输出列表元素和序号（序号从100开始）
for index,i in enumerate(li):
    print(100 + index,":{0}".format(i))
# 	请使用for循环输出列表的所有元素
for i in li:
    print(i)