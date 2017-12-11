# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import  subprocess

a = subprocess.run(['df','-h'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(a.stdout)