# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:41:29 2022

@author: Doshite368
"""

import string

num = int(input())

if num == 0:
    print(string.ascii_lowercase)
elif num == 1:
    print(string.ascii_uppercase)


import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789