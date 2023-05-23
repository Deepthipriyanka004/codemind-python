n=int(input())
res=0
while(n>0):
    k=n%10
    res=max(res,k)
    n=n//10
print(res)