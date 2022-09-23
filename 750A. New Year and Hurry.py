counter=5
problems_solved=0
the_Inbetween=0
hurry=list(map(int,input().split()))
if(1<=hurry[0]<=10 and 1<=hurry[1]<=240):
    the_Inbetween=240-hurry[1]
    for i in range (1,hurry[0]+1):
        if(the_Inbetween<counter):
            break 
        the_Inbetween-=counter
        counter=5*(i+1)
        problems_solved+=1
    print(problems_solved)