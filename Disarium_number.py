n=int(input())
k=str(n)
s=0

for i in range(len(str(n))):
    s+=int(k[i])**(i+1)
    
if(s==n):
    print(True)
else:
    print(False)