# -*- coding:utf-8 -*-
# AUTHER   @ Alvin
# 手写进度条
import sys,time
for ii in range(101):
    sys.stdout.write('\r')  #每一次清空原行。
    sys.stdout.write("%s%%  |%s|"%(int(int(ii)/100*100),int(int(ii)/100*100) * '#'))     #一共次数除当前次数算进度
    sys.stdout.flush()      #强制刷新到屏幕
    time.sleep(0.05)