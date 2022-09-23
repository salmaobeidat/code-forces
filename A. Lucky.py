testcases=int(input())
for i in range (testcases):
    part1sum=0
    part2sum=0
    ticket=list(map(int,input().strip()))
    if (len(ticket)!=6):
        break
    for s in range(0,3,1):
        part1sum+=ticket[s]
    for j in range(3,6,1):
        part2sum+=ticket[j]
    if(part1sum==part2sum):
        print("YES")
    else:
        print("NO")
          