# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:00:23 2022

@author: obeid
"""

n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
leftover=0
if(len(a)==m):
    leftover=a[0]-1
    for i in range(len(a)-1):
        if(a[i]>a[i+1]):
            leftover+=n-a[i]+a[i+1]
        elif(a[i]<a[i+1]):
            leftover+=a[i+1]-a[i]
        elif(a[i]==a[i+1]):
            continue
    print(leftover)