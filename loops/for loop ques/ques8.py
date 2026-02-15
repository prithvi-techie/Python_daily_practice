# print the sum of all even and all odd number in a arange seperately
n = int(input("Enter your number: "))
even = 0
odd = 0
for i in range(1,n+1):
    if i%2==0:
        even = even +i
    else:
        odd = odd+i
print(f"sum of even numbers:{even}")
print(f"sum of odd numbers:{odd}")