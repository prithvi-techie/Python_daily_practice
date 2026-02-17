# prime or not
n = int(input("Enter the number: "))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count = count +1    #count +=1 
if count == 2:
    print("The numeber",n,"is an prime number")
else:
    print(f"The numebr {n} is not an prime number")
