
"""for i in range(1,5):
    ch=64+i
    for j in range(1,i+1):
        print(chr(ch),end="")
        ch-=1
        
    print()"""

"""for i in range(1,5):
    for j in range(1,8):
        if j<=5-i or j>=3+i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""

"""ch=65
for i in range(1,5):
    for j in range(1,8):
        if j<=i or j>=8-i:
            
            print(chr(ch),end=" ")
        else:
            print(" ",end=" ")
    ch+=1
    print()"""
# diamond pattern
"""for i in range(1,4):
    for j in range(1,6):
        if j>=4-i and j<=2+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(1,3):
    for j in range(1,6):
        if j>=i+1 and j<=5-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""