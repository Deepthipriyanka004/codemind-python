def selff(a):
    n=a
    l=len(str(a))
    c=0
    while(a):
        k=a%10
        if k!=0:
            if n%k==0:
                c+=1
        a=a//10
    if c==l:
        return True
    return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if selff(i):
        print(i,end=" ")