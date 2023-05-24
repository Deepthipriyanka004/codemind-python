def pal(n):
    n=str(n)
    rev=n[::-1]
    if int(n)==int(rev):
        return True
    return False
n=int(input())
c=1
d=0
t=False
F=False
while n:
    if pal(n-c)and pal(n+c):
        d+=1
        break
    elif pal(n-c):
        F=True
        break
    c+=1
if d==1:
    print(n-c,n+c)
elif(F==True):
    print(n-c)
elif(l==True):
    print(n+1)