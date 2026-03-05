#54321
#4321
#321
#21
#1

for i in range(1,6):
    for j in range(1,6):
        if j<=6-i:
            print(6-j,end="")
        else:
            print(" ",end="")
    print()