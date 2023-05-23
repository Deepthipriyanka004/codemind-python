n=int(input())
c=[]
d=[]
while n:
    k=n%10
    c.append(k)
    n=n//10
for i in c:
    if i not in d:
        d.append(i)
if len(c)==len(d):
    print("Unique Number")
else:
    print("Not Unique Number")
    