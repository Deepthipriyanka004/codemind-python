n=int(input())
k=n*n
n=str(n)
m=n[::-1]
l=int(m)*int(m)
l=str(l)
x=int(l[::-1])
if x==k:
    print(True)
else:
    print(False)