h,s,sl=map(int,input().split())
if h>50 and s>60 and sl>100:
    print(10)
elif h>50 and s>60 and sl<100:
    print(9)
elif h<50 and s>60 and sl>100:
    print(8)
elif h>50 and s<60 and sl>100:
    print(7)
elif h>50 or s>60 or sl>100:
    print(6)
else:
    print(5)