n=int(input())
m=0
if n<0:
    m=n*(-1)
n=str(n)
m=str(m)
rev=n[::-1]
rev1=m[::-1]
if int(n)<1:
    print(int(rev1)*-1)
else:
    [print(int(rev))]