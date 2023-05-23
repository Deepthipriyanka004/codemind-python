n=int(input())
c=[]
k=0
a=0
b=1
d=a+b

while k<n:
    c.append(a)
    a=b
    b=d
    d=a+b
    k+=1
print(*c)