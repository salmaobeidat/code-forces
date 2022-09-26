# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 00:51:22 2022

@author:salma obeidat
"""
locationX=0
locationY=0
for i in range(5):
    line=list(map(int,input().split()))
    for j in range(5):
        if(line[j]==1):
            locationX=i
            locationY=j
            break
if(locationX==2 and locationY==2):
    print(0)
else:
    moves=abs(locationX-2)+abs(locationY-2)
    print(moves)