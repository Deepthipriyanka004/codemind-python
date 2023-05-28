n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    k=sorted(b)
    if(k==b):
        print(0)
    else:
        print(max(b)-min(b))