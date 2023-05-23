n=int(input())
k=0
a=0
b=1
c=a+b
d=[]
while(k<n):
    d.append(a)
    a=b
    b=c
    c=a+b
    k+=1
if n in d:
    print(True)
else:
    print(False)
