m,n=map(int,input().split())
num=m
m=str(m)
c=n-1
d=len(m)-n-1
x=""
y=""

for i in range(len(m)):
    if c>=i:
        x+=str(m[i])
    elif d<i:
        y+=str(m[i])
        d+=1
print(abs(int(x)-int(y)))
    