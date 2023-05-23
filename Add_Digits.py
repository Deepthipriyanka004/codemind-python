n=int(input())
s=0
while(n):
    k=n%10
    s+=k
    n=n//10
    if n==0 and s>9:
        n=s
        s=0
print(s)    