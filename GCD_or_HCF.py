n,m=map(int,input().split())
k=max(n,m)
res=0
for i in range(1,k+1):
    if n%i==0 and m%i==0:
        res=max(res,i)
print(res)        