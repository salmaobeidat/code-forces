# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 01:04:48 2022

@author: salma obeidat
"""

#mishka:mishka's winnings counter
#chris:chris's winnings counter
mishka=0
chris=0
#n: number of rounds
n=int(input())
for i in range(n):
    s,o=list(map(int,input().split()))
    if(s>o):mishka+=1
    if(s<o):chris+=1
    if(s==o):continue
if(mishka>chris):print("Mishka")
if(mishka<chris):print("Chris")
if(mishka==chris):print("Friendship is magic!^^")