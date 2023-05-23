def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
n=int(input())
for i in range(n):
    m=int(input())
    print(fact(m))
        