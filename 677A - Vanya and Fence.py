# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:56:27 2022

@author: obeid
"""

n,h=list(map(int,input().split()))
if(1<=n<=pow(10,3) and 1<=h<=pow(10,3)):
    a=list(map(int,input().split()))
    counter=0
    if(len(a)==n):
        for i in range(len(a)):
            if(a[i]<=h):
                counter+=1
            else:
                counter+=2
        print(counter)