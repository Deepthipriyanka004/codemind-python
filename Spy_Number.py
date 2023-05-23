n=int(input())
s=0
d=1
while(n):
    k=n%10
    s+=k
    d*=k
    n=n//10
if s==d:
    print("Spy Number")
else:
    print("Not Spy Number")