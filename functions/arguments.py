# types of arguments (arguments = avlue)

# 1)positional arguments - Positional arguments are arguments that are assigned to parameters based on their position (order)

"""def sub(a,b):
    print(f"The subtraction of given numbers is: {a-b}")
sub(12,6)
sub(4,12)"""

# 2) keyword argument - it does not follow continuation(order)

"""def hello(name,age):
    print(f"Your name is {name} and Your age is {age}")

hello("vashu",22)  # following continuation(order)
hello(12,"vashu")  # following continuation - positional argument

hello(age=12,name="vashu")  # keyword argument
age=12 -- keyword argument"""


# 3) default argument
# here a = ___ and b = 4 (given already)(if given another will accept that)
"""def sum(a,b=4):
    print(f"The sum of given numbers is {a+b}")

sum(12)    #if given another value of b it will reasign(change)"""  