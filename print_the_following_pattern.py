n=int(input())
m={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
for i in range(1,n+1):
    for j in range(1,n+1):
        print(m[i],end=" ")
    print()    