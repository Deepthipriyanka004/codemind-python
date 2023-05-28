s=input()
s=s.split(":")
s=list(s)
m=int(s[-1])*6
h=((int(s[-2])*60)+int(s[-1]))*0.5
if abs(h-m)>180:
    print(360-abs(h-m))
else:
    print(h-m)