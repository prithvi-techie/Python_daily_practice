# # reverse a string without using in built func.
# a=  "Prithvi"
# print(a[::-1])

#or

a = "Vashu"

for i in range(len(a)-1,0,-1): # start:-1 :: print total length -1
    print(a[i])                 # stop:-1 :: why not 0 bcz loop have to go to the last
                                # skip:-1 :: to reverse the sring