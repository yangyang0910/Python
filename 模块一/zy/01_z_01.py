menus = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '通天苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}


# 1.	可依次选择各子菜单
# 2.	可从任意一层往回退到上一级
# 3.	可从任意一层退出程序
count = ""
Superior = ""
while True:
    menu = input("请选择(S返回上一级)")
    if menu in menus:
        count = menus[menu]
    elif menu == "q":
        break
    elif menu in count:
        Superior = count
        count = count[menu]
    elif menu == "S":
        count = Superior
    else:
        print("输入有误！")
    print(count)



























