def prime(n):
    c=0
    if n<=1:
        return False
    for i in range(1,n//2+1):
        if n%i==0:
            c+=1
    if c==1:
        return True
    return False
n=int(input())
a=n
l=len(str(a))
c=0
if prime(n)==False:
    print("Not Mega Prime")
else:
    while n:
        k=n%10
        if prime(k) and k!=0:
            c+=1
        n=n//10
    if l==c:
        print("Mega Prime")
    else:
        print("Not Mega Prime")