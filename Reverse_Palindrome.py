def rev(a):
    b=str(a)
    return int(b[::-1])
a=int(input())
while True:
    b=rev(a)
    c=b+a
    if rev(c)==c:
        print(c)
        break
    else:
        a=c