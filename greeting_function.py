# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 23:14:33 2022

@author: Doshite368
"""

def Func1(name,age):
    age = int(age)
    name = str(name)
    if age < 10:
        print("안녕 {0}".format(name))
    elif age >= 10 and age < 20:
        print("안녕하세요 {0}".format(name))
    else:
        print("안녕하십니까 {0}".format(name))
        
Func1("소향",21)