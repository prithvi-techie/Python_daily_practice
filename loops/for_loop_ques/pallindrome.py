#check string is pallindrome or not
# sidha ulta kahi se bhi padho same aata h ex- naman

a = input("Enter your name: ")
b =""
for i in range(len(a)-1,-1,-1):
    b += a[i] # to store ulti string in a single line
if b == a:
    print("Pallindrome")
else:
    print("not a pallindrome")
    