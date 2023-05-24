import math
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    for i in range(int(math.floor(math.sqrt(a))),b//2+1):
        if((i*i)%b)==a:
            print(i)
            break
    else:
        print(-1)
    