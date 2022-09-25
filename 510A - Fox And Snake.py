# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 21:26:06 2022

@author: obeid
"""
counter2=2
counter4=4
n,m=list(map(int,input().split()))
if(3<=n and m<=50 and n%2!=0):
    for i in range(1,n+1):
        if(i%2!=0):
            for i in range(m):
                print('#',end="")
            print()
        elif(i==counter2 and i%2==0):
            counter2+=4
            for j in range(m-1):
                print('.',end="")
            print('#')
        elif(i==counter4 and i%2==0 ):
            counter4+=+4
            print("#",end="")
            for k in range(m-1):
                print(".",end="")
            print()
            
