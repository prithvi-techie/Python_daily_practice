#################### odd even from list
# l = [1,2,3,4,5,6]
# print("even :")

# for i in l:
#     if i%2==0:
#         print(i)

# print("odd :")

# for i in l:
#     if i%2!=0:
#         print(i)

# #mean of list
# sum =0
# l = [1,2,3,4,5]
# for i in l:
#     sum+=i
#     average=sum/len(l)
# print(int(average))

####################find the greatest element and print its index to 

# l = [14,15,245,486,45,75,154]
# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i]>largest:
#         largest=l[i]
#         index=i
#     else:
#         continue
# print(f"largest no : {largest}, index of largest no: {index}")

#################### find the 2nd greatest number (using 2 loops)

# l =[451,865,471,259,954,254,15,145]
# largest = l[0]

# for i in range(len(l)):
#     if l[i]>largest:
#         largest = l[i]
#     else:
#         continue
# l.remove(largest)
# s_largest=l[0]
# for i in range(len(l)):
#     if l[i]>s_largest:
#         s_largest=l[i]
#     else:
#         continue
# print(l)
# print(f"largest: {largest}, second largest: {s_largest}")

#################### using algo

# l = [1,5,7,4,10]
# largest = l[0]
# indexl = 0
# s_largest = l[0]
# indexs = 0
# for i in range(len(l)):
#     if l[i]>largest:
#         s_largest = largest
#         indexs = indexl
#         largest=l[i]
#         indexl = i
        
#     elif l[i]>s_largest:
#         s_largest = l[i]
#         indexs = i
# print(l)
# print(f"largest: {largest} index: {indexl}, second largest: {s_largest} index: {indexs}")

####################check if list is sorted or not
# l  = [12,13,14,15]
# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("not sorted")
#         break
# else:
#     print("sorted")
