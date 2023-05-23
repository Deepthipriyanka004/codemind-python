n=int(input())
k=len(str(n))
n=str(n)
if(k<10 or n[0]==0):
    print("Invalid")
else:
    print("Valid")