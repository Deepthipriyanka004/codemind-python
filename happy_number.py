n=int(input())
sum=0
while n:
    k=n%10
    sum=sum+(k*k)
    n=n//10
    if n==0 and sum>9:
        n=sum
        sum=0
if sum==1 or sum==7:
    print(True)
else:
    print(False)