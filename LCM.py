def gcd(n,m):
    k=max(n,m)
    res=0
    for i in range(1,k):
        if n%i==0 and m%i==0:
            res=max(res,i)
    return res
n,m=map(int,input().split())
print((int(m)*int(n))//(int(gcd(m,n))))