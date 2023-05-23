t=int(input())
for i in range(t):
    a=int(input())
    n=a**0.5
    if n-int(n)==0.00:
        print(True)
    else:
        print(False)