n=int(input())
m=list(map(int,input().split()))
a=sum(m)
while(n):
    if(a%n==0):
        print(n)
        break
    n-=1