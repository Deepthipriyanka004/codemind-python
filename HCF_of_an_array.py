n=int(input())
m=list(map(int,input().split()))
k=min(m)
c=0
for i in range(1,k+1):
    t=True
    for j in m:
        if j%i!=0:
            t=False
            break
    if t==True and i>c:
        c=i
print(c)        