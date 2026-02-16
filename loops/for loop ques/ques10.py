# accept a number and check if it a perfect number or not
"""perfect number- a number whose sum of factor is equal to the 
number itself {ex - 6 , fact: 1,2,3,,1+2+3=6}"""
n = int(input("Enter the number: "))
sum =0
for i in range(1,n):
    if n%i==0 :
        sum = sum+i
if sum == n:
    print(f"Yes it is a perfect number:{sum}")
else:
    print("This is not a perfect numebr")