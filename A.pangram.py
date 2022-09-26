# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:16:23 2022

@author: obeid
"""
import string
x=int(input())
string1=input().lower()
if(set(string1)==set(string.ascii_lowercase)):
   print("YES")
else:
    print("NO")
    
#why set? because it prevent all repetation in any sentence
#string.ascii_lowercase is all alphabet 