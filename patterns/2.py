"""
A
AB
ABC
ABCD"""

for i in range(1,5):
    ch=65
    for j in range(1,5):
        if j<=i:
            print(chr(ch),end="")
            ch+=1
    print()