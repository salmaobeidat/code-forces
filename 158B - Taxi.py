from collections import Counter
import math
minx=0
n=int(input())
if (1<=n<=pow(10,5)):
    s=list(map(int,input().split()))
    if(len(s)==n):
        c1=s.count(1)
        c2=s.count(2)
        c3=s.count(3)
        c4=s.count(4)
        minx+=c4
        minx+=c3
        c1-=c3
        if(c1<0):c1=0
        if(c2%2==0):
            c2=c2//2
            minx+=c2
        else:
            c2=c2//2+1
            minx+=c2
            c1=c1-2
            if(c1<0):c1=0
        c1=int(math.ceil(c1/4))
        minx+=c1
        print(minx)

