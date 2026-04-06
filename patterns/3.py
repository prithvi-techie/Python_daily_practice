"""
A
BA
CBA
DCBA"""

for i in range(1,5):
    ch=64+i
    for j in range(1,5):
        if j<=i:
            print(chr(ch),end="")
            ch-=1
    print()