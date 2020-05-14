n=5
print("\n====================================================\n")
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("\n====================================================\n")
for i in range(n,0,-1):
    for j in range(1,n+1):
        if(j<i):
            print("*",end="")
    print()
print("\n====================================================\n")
for i in range(1,n+1):
    for j in range(n,0,-1):
        if(j<=i):
            print("*", end="")
        else:
            print(" ",end="")
    print()
print("\n====================================================\n")
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if(j<=i):
            print("*", end="")
        else:
            print(" ", end="")
    print()

