n=int(input())
c=[]
for i in range(1,n+1):
    c.append(str(i))
for i in range(len(c)):
    print("".join(c))
    c.pop()