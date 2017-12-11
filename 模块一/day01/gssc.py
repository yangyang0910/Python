# -*- coding:utf-8 -*-
# AUTHER   @ Alvin


name = input("Name:")
age = input("Age:")
job = input("Job:")
hometown = input("Hometown:")

print("")
print("Name：：",name)
print('''
------ info of ''',name,'''------
Name:''',name,'''
Age:''',age,'''
Job:''',job,'''
Hometown:''',hometown,'''
------- end ----------------------
''')

print('''
------ info of %s------
Name: %s
Age: %s
Job: %s
Hometown: %s
------- end ----------------------
''' % name,name,age,job,hometown)