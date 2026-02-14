temp = int(input("Enter the temprature in celcius: "))

if temp > 40:
    print("very hot")
elif temp > 30:
    print("Hot")
elif temp > 20:
    print("pleasent")
elif temp > 10:
    print("cold")
elif temp > 0:
    print("very cold")
else: 
    print("freezing cold")