n=int(input())
counter=0
if(1<=n<=50):
    stones=input()
    if(len(stones)==n):
        for i in range(len(stones)-1):
            if(stones[i]==stones[i+1]):
                counter+=1
        print(counter)