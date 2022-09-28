# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 01:37:03 2022

@author: salma obeidat
"""

t=int(input())
for i in range(t):
    operations=0
    a,b,n=list(map(int,input().split()))
    while(max(a,b)<=n):
        if(a<b):
            a+=b
        else:
            b+=a
        operations+=1  
    print(operations)
        
        