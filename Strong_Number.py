def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
n=int(input())
a=n
summ=0
while(n):
    k=n%10
    summ+=fact(k)
    n=n//10
if summ==a:
    print("The number",a,"is a strong number")
else:
    print("The number",a,"is not a strong number")