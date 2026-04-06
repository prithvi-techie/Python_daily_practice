#1st line
for i in range(1,2):
    for j in range(1,9):
        if (j<=3 and j>=2) or (j<=8 and j>=7):
            print("*",end="")
        else:
            print(" ",end="")
    print()
# 2nd line
for i in range(1,2):
    for j in range(1,10):
        if (j<=4 and j>=1) or (j<=9 and j>=6):
           print("*",end="")
        else:
            print(" ",end="")
    print()
# 3rd line
for i in range(1,10):
    print("*",end="")
print()
# down part
for i in range(1,4):
    for j in range(1,10):
        if j>=i+1 and j<=9-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()


        