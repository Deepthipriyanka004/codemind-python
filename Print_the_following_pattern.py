n=int(input())
for i in range(1,n+1):
    a=i
    for j in range(1,n+2-i):
        print(a,end=" ")
        a+=1
    print()    