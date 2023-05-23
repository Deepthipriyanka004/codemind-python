n=int(input())
a=n
k=n*n
k=str(k)
n=str(n)
if k.endswith(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")