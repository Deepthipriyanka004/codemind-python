s=input()
h=int(s[:2])
m=int(s[3:])
s=abs(30*h-5.5*m)
if(s>180):
    s=360-s
print(s)    