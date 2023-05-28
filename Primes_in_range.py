def prime(n):
    a=int(n**0.5)
    for i in range(2,a+1):
        if n%i==0:
            return False
    else:
        return True
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if i==1:
        continue
    if prime(i):
        c+=1
print(c)        