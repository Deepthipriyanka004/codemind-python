def pal(n):
    n=str(n)
    rev=n[::-1]
    if int(n)==int(rev):
        return True
    return False
t=int(input())
for i in range(t):
    n=int(input())
    if pal(n):
        print(True)
    else:
        print(False)