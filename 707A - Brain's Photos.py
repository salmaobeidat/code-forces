# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:18:22 2022

@author: salma obeidat
"""

color=0
row,column=list(map(int,input().split()))
for j in range(row):
    s=list(map(str,input().upper().split()))
    for x in range(column):
        if(s[x]=='C' or s[x]=='Y' or s[x]=='M'):
            color+=1
            break
if(color!=0):print("#Color")
else:print("#Black&White")
    
