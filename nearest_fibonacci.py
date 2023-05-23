n=int(input())
v=[]
a=0
b=1
v.append(a)
v.append(b)
c=0
for i in range(n):
    c=a+b
    a=b
    b=c
    v.append(c)
    if c>n:
        break
if abs(v[-1]-n)>abs(v[-2]-n):
    print(v[-2])
elif abs(v[-1]-n)==abs(v[-2]-n):
    print(v[-2],v[-1])
else:
    print(v[-1])