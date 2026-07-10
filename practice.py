n = int(input("Enter the num: "))
pallin=0
while n>0:
    pallin = n%10
    n=n//10
if n == pallin:
    print("pallindrome")
else:
    print("not")
