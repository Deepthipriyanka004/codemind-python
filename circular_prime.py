def prime(n):
    c=0
    for i in range(1,n//2):
        if n%i==0:
            c+=1
    if c==1:
        return True
    return False
n=int(input())
a=n
n=str(n)
rev=n[::-1]
rev=int(rev)
if prime(a) and prime(rev):
    print("circular prime")
elif prime(a)==True and prime(rev)==False:
    print("prime but not a circular prime")
elif prime(a)==False:
    print("not prime")