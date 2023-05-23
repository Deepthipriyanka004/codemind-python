n=int(input())
k=n*n
s=0
while k:
    l=k%10
    s+=l
    k=k//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")