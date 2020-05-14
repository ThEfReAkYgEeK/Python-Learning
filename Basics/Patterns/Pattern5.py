n=5
for i in range(n-1,-n,-1):
    if(i<=0):
        k=-i
    else:
        k=i
    for j in range(0,n):
        if(j>=k):
            print("* ",end="")
        else:
            print(" ",end="")
    print()

print("\n=====================================\n")

for i in range(n-1,-n,-1):
    if(i<0):
        k=-i
    else:
        k=i
    for j in range(n-1,-1,-1):
        if(j<=k):
            print("* ",end="")
        else:
            print(" ",end="")
    print()
