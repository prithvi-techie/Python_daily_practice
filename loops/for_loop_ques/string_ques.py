# calculate all the special characters, numbers and alphabets from the given string
a = "1213!#@#!@dasmn"

alpha = 0 #alphabets
chr = 0 #special charcaters
dig = 0 #digits

for i in a:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        alpha+=1
    else:
        chr+=1
print("Special characters: ",chr)
print("digits: ",dig)
print("Alphabets",alpha)