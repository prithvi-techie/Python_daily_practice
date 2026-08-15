#python dic to merge two diff dict
# d1 = {10:100,20:200,30:300}
# d2 = {40:400,20:500,50:600}

# # way 1
# m = d1.update(d2)
# print(d1)

# # way 2
# for i in d1:
#     d2[i] = d1[i]
# print(d2)

# #program to sum all the values in dict
# d1 = {10:100,20:200,30:300}
# sum = 0
# for i in d1:
#     sum+=d1[i]
# print(sum)

#count the frequency of each element in list
# a = [1,2,3,4,4,5,5,6]
# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# write a python program to combine two dictionary  by adding values for common keys
d1 = {1:10,2:20,3:30}
d2 = {4:40,1:10,2:20}

for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i] = d2[i]
print(d1)