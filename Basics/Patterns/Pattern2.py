r=c=int(input("Enter the number of rows"))
for i in range(1,r+1):
    for j in range(1,c+1):
        print("*",end=" ")
    c=c-1
    print()
