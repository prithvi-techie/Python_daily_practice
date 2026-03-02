# Print numbers from 1 to 20.
"""for i in range(1,21):
    print(i)"""

#Print all odd numbers between 1 and 30.
"""for i in range(1,31):
    if i%2 !=0:
        print(i)
        #or
a = 1
for i in range(1,31):
    if i%2==0:
        a = a+i
    else:
        print(i)"""

#Print the multiplication table of any number (user input) up to 10.
"""n = int(input("Enter athe number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")"""

#Find the sum of all numbers from 1 to n (n given by user).
"""a = 0
n = int(input("Enter the number: "))
for i in range(1,n+1):
    a = a+i
print(a)"""

#Find the factorial of a number using a for loop.
"""n  = int(input("Enter a number: "))
a = 1
for i in range(1,n+1):
    a = a*i
print(a)"""

#Count how many numbers between 1 and 100 are divisible by 7.
"""count = 0
for i in range(1,100):
    if i%7==0:
        count = count +1
print(count)"""

