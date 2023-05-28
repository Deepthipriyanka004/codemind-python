a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    t=sorted(c)
    if c==t:
        print(0)
    else:
        y=t[-1]-t[0]
        print(y)