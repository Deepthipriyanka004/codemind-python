def odd(n):
    if n%2==0:
        return False
    return True
n=int(input())
od=0
evn=0
c=0
while n:
  k=n%10
  c+=1
  n=n//10
  if odd(k):
     od+=1
  else:
     evn+=1
if c==od:
    print("Odd")
elif c == evn:
    print("Even")
else:
    print("Mixed")
            
    