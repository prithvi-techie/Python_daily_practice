# Going from 20 to 50 
""" for i in range(20,51): # default skip value:1
    print(i) """

# Going from 16 to 1
""" for i in range(16,0,-1):
    print(i) """

# Going from -3 to -15
""" for i in range (-3,-16,-1):
    print(i) """

# Table of 5
""" for i in range (5,51,5):
    print(i) """

# Table of given number
"""n = int(input("Which number you want to multiply? "))
for i in range(n,n*10+1,n):
    print(i)"""

# loops on string
"""
a = "Prithvi"
for i in range(7):
    print(a[i]) # if i write only(i) it will give 1,2,3 to 6 bcz i gives the character at postion
                                                            # and a[i] gives the character"""

# direct acces in string
""" a = "prithvi"
for i in a:
    print(i) """

# practice
# numbers 1 to 20 - even numbers
"""for i in range(2,21,2):
    print(i)"""

# number input table (_x1=_)
"""num=int(input("Enter the number to get table: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)"""

# practice
"""for i in range(1,21):
    if i ==7:
        continue
    else:
        print(i)"""
# factorial
"""n = int(input("Enter the numebr to find factorial: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)"""

# find summ of all the factorials of number
"""n = int(input("Enter no. to find sum of facto: "))
sum =0
for i in range(1,n+1):
    if n%i==0:
        sum = sum+i
print(sum)"""

# print natural number upto n
"""n = int(input("Enter your number: "))
for i in range(1,n+1):
    print(i)
"""
#take a number as input and print its table
"""n = int(input("Enter your number: "))
for i in range(1,11):
    print(n,"x",i,"=",n*1)"""

#sum upto n numbers
"""n = int(input("enter the number: "))
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(sum)"""

# find if its perfect number or not
# perfect number = sum of its factors
"""n = int(input("Enter the number: "))
sum = 0
for i in range(1,n):
    if n%i==0:
        sum = sum+i
if sum==n:
    print("perfect")
else:
    print("not perfect")"""

#sum of even and odd numbers separately
"""n = int(input("Enter the number: "))
odd = 0
even = 0
for i in range(1,n+1):
    if i%2==0:
        even = even+i
    else:
        odd = odd+i
print("sum of even numbers:",even)
print("sum of odd numbers:",odd)
print("even: ",even+i)"""

"""# print 1 to 30 numbers
#for loops
for i in range(1,31):
    print(i,end=",")

# while loop
a = 0
while a<=30:
    a+=1
    print(a,end=",")"""

"""# pallindrome
a = int(input("Enter a number: "))
copy = a
rev = 0
while a>0:
    rev = rev*10 +a%10
    a = a//10
if copy<0:
    print("negative numbers are not pallindrome")
elif copy==rev:
    print("pallindrome")
else:
    print("not a pallindrome")"""

#1 to 10
"""for i in range(1,11):
    print(i)"""

#1 to 20 even numbers
"""for i in range(1,21):
    if i%2==0:
        print(i)"""

# tabel of 7 (7x1=7)
"""n = 7
for i in range(1,11):
    print(n,"x",i,"=",n*i)"""

#find the sum of numbers from 1 to 50
"""sum = 0
for i in range(1,51):
    sum = sum+i
print("sum is:",sum)"""

#factorial
"""n = int(input("Enter the number to find factorial: "))
fcat = 1
for i in range(1,n+1):
    fcat = fcat*i
print(fcat)"""

#while loops 1 to 10
"""i = 1
while i<11:
    print(i)
    i+=1"""
#