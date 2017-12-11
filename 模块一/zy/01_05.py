tu = ("alec", "aric", "Alex", "Tony", "rain")

# 	计算元祖长度并输出
print(len(tu))
# 	获取元祖的第二个元素,并输出
print(tu[1])
# 	获取元组的第1-2个元素，并输出
print(tu[0:2])
# 	请使用for输出元组的元素
for i in tu:
    print(i)
# 	请使用for\len\range输出列表索引
for index,i in enumerate(range(len(tu))):
    print(index)
# 	请使用enumrate输出列表元素和序号（序号从10开始）
for index,i in enumerate(tu):
    print(10+index,":%s" % (i) )