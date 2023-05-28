n=int(input())
l=[]
s=2
l.append(s)
for i in range(n+n):
    s*=2
    l.append(s)
    if s>n:
        break
if n in l:
    print(n-n)
elif abs(l[-1]-n)>abs(l[-2]-n):
    print(abs(l[-2]-n))
elif abs(l[-1]-n)<abs(l[-2]-n):
    print(abs(l[-1]-n))
    
    
    