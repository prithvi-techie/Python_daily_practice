# accept a number and print its reverse
"""a = int(input("Enter the number: "))
while a>0:
    print(a%10,end="")
    a = a//10
"""
# or

rev = 0 
a = int(input("Enter the numbe: "))
while a>0:
    rev = a%10
    a = a//10
    print(rev)
