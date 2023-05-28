n=int(input())
a="*"
c=n
if(n<=2):
    print("The pattern is not possible")
else:
    for i in range(1,n+1):
        print(a*i)
        if i==n:
            t=i-1
            while t:
                print(t*a)
                t-=1
