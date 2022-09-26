# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 23:51:35 2022

@author: salma obeidat
"""

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    odd=0
    for i in range(len(a)):
        if(a[i]%2!=0):
            odd+=1
    if(odd==n):
        print("YES")
    else:
        print("NO")
        
#the sum of even and odd numbers is odd ,so if we have
#2n set we n even numbers and n odd numbers to let me have
#n sets with odd sum for each 