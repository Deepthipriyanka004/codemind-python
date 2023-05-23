def prime(n):
    c=0
    for i in range(1,n//2+1):
        if n%i==0:
            c+=1
    if c==1:
        return True
    return False
n=int(input())
m=int(input())
for i in range(n,m):
    if prime(i):
        print(i)