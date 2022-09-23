n=int(input())
s=[]
if(1<=n<=pow(10,5)):
    counter=0
    for i in range(n):
        x=input()
        s.append(x)
    for j in range(len(s)-1):
        if(s[j]!=s[j+1]):
            counter+=1
    print(counter+1)