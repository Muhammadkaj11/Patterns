rowsize=int(input("enter the number of rows:"))
if rowsize%2==0:
    halfDiamRow=int(rowsize/2)
else:
    halfDiamRow=int(rowsize/2)+1
space=halfDiamRow-1
for i in range(1,halfDiamRow+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1, halfDiamRow):
    for j in range(1, space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range(1,2*(halfDiamRow-i)):
        print(end=str(num))


    
