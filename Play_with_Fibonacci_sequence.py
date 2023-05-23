n=int(input())
a=0
b=1
l=[]
l.append(a)
l.append(b)
for i in range(n-2):
    c=a+b
    l.append(c)
    a=b
    b=c
print(*l)    