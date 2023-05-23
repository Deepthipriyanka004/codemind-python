def pal(n):
    n=str(n)
    rev=int(n[::-1])
    n=int(n)
    if rev==n:
        return True
    else:
        return False
        
a=int(input())
b=int(input())
for i in range(a,b+1):
    if pal(i):
        print(i,end=" ")