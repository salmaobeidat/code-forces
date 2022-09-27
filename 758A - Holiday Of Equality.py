# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 01:47:06 2022

@author: salma obeidat
"""


moves=0
#n:number of citizens
n=int(input())
if(1<=n<=100):
    a=list(map(int,input().split()))
    if(len(a)==n):
        maX=max(a)
        a.remove(maX)
        for i in range(len(a)):
            moves+=(maX-a[i])
        print(moves)