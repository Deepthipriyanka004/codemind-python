import math
for _ in range(int(input())):
    n,x,y,k=[int(x) for x in input().split()]
    a=int(n/x)
    b=int(n/y)
    c=int(n/((x*y)//math.gcd(x,y)))
    if a+b-(2*c)>=k:
        print("Win")
    else:
        print("Lose")