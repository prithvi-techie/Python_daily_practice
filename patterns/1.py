"""
A
BC
DEF
GHIJ"""
ch=65
for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print(chr(ch),end="")
            ch+=1
    print()

