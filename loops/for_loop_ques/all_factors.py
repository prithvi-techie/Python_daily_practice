# print all the factors of a number 
n = int(input("Enter the number: "))
"""12-> 2,3,4,6,12"""
for i in range(1,n+1):
    if n%i==0:
        print(i)
    else:
        continue