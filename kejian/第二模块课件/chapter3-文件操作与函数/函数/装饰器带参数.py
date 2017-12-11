# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
user_status = False  # 用户登录了就把这个改成True
def login(auth_type): #qq

    def outer(func): #henan
        def inner(*args,**kwargs): #3p
            _username = "123"  # 假装这是DB里存的用户信息
            _password = "abc"  # 假装这是DB里存的用户信息
            global user_status
            if user_status == False:
                username = input("user:")
                password = input("pasword:")

                if username == _username and password == _password:
                    print("welcome login....")
                    user_status = True
                else:
                    print("wrong username or password!")
            else:
                print("用户已登录，验证通过...")

            if user_status:
                func(*args,*kwargs) #3p
        return inner
    return outer

@login('qq') # henan = login('qq')(henan) = inner
def henan():
    print("----河南专区----")
henan()




