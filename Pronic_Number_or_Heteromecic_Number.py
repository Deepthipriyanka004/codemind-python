n=int(input())
t=False
for i in range(n+1):
    if i*(i+1)==n:
        t=True
        break
if t==True:
    print("YES")
else:
    print("NO")