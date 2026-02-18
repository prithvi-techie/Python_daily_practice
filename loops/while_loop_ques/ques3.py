# check if a number is pallindromic numebr(if number and its reverse are equal)
a = int(input("Enter the numebr: "))
copy = a    # copy=variable
rev = 0
while a>0:
    rev = rev*10+a%10    #3:51:30 ( last digit * 10 + reverse(a%10))
    a = a//10
if copy<0:
    print("negative numbers are not pallindrome")
elif copy == rev:
    print("pallindorme")
else:
    print("not a pallindrome")