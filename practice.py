# class Factort:
#     def __init__(self,material,size):
#         self.material = material
#         self.size = size
# reebok = Factort("nylon",8)
# campus =  Factort("cotton",5)

# print(reebok.material)

# class Animal :
#         name = "lion" # class attribute 

#         def __init__(self,age): 
#                 self.age = age  #instance attribute
        

# class Factory:
#     def __init__(self,materials):
#         self.materials = materials

# class PuneFactory(Factory):
#     def __init__(self, materials, color):
#         super().__init__(materials)
#         self.color = color

# class BhopalFactory(PuneFactory):
#     def __init__(self, materials, color,size):
#         super().__init__(materials, color)
#         self.size = size

# class Bank():
#     def __init__(self):
#         self.name = "adasrsh"
#         self._age = 21
#         self.__salary1 = 40000

# obj = Bank()
# obj.Bank__salary1 = 15125
# print(obj.__salary1)

# class BankAccount():
#     def __init__(self,balance):
#         self.__balance = balance

#     def deposit(self,amount):
#         self.__balance += amount

#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.__balance -= amount
#         else:
#             print("Inefficient Funds")

#     def get_balance(self):
#         return self.__balance

# acc = BankAccount(100)
# acc = BankAccount(70)
# print(acc.get_balance())   

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#     def deposit(self,amount):
#         self.__balance += amount
#     def withdraw(self,amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insuffiecient balance")
#     def get_balance(self):
#         return self.__balance
# acc = BankAccount(100)
# print(acc.get_balance())
# acc.deposit(20)
# print(acc.get_balance())
# acc.withdraw(140)
# print(acc.get_balance())

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance
#     def deposit(self,amount):
#         self.__balance += amount
#     def withdrawl(self,amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Inssuficient Funds")
#     def get_balance(self):
#         return self.__balance
# e = BankAccount(100)
# print(f" Your current balance: {e.get_balance()}")
# e.deposit(10)
# print(f" Your current balance: {e.get_balance()}")
# e.withdrawl(500)
# print(f" Your current balance: {e.get_balance()}")

# class Vehicle:
#     def wheels(self,wheel):
#         self.wheel = wheel
#         print(f"This vehicle has {wheel} wheel")
# class Car(Vehicle):
#     pass

# e = Vehicle()
# e.wheels(10)

#Alright, moving on.

# **M4 (Practical):** Create a `Person` class with `__init__(self, name, age)` that stores both. 
# Then create a `Student` class that inherits from `Person`, adds a `roll_no` attribute, and 
# uses `super().__init__()` to set `name` and `age`. Add a method `show_details()` in `Student` 
# that prints all three (name, age, roll_no).

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Student(Person):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no

#     def show_details(self):
#         print(f"name: {self.name} age: {self.age}, roll no: {self.roll_no}")

# e = Student("vashu", 13 , 908)
# e.show_details()

# E4 (Practical): Write two unrelated classes, Circle and Square (no shared parent), 
# each with a method area() 
# that calculates and prints their area (assume you're given radius for Circle and 
# side for Square in __init__). Then loop through a list containing one of each and call area() on both.

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius * 2 * 3.14
#         print(f"Area of circle: {self.radius}")

# class Square:
#     def __init__(self,side):
#         self.side = side * side
#         print(f"area os sqaure : {self.side}")

# area = Circle(2)
# area = Square(2)

# class Dog:
#     def speak(self):
#         print("bark")

# class Cat:
#     def speak(self):
#         print("Meow")

# class Car:
#     def speak(self):
#         print("O")

# things = [Cat(),Dog(),Car(),"Hello"]
# for t in things:
#     t.speak()

# def Decorate(func):
#     def wrapper():
#         print("0")
#         func()
#         print("2")
#     return wrapper

# @Decorate
# def Count():
#     print("1")

# Count()

#printing 0 1 2 in dieerent ways
#a)
# for i in range(3):
#     print(i)
#     i+=1

#b)
# i = 0
# while i<3:
#     print(i)
#     i += 1

#c)
# def Decorate(func):
#     def wrapper():
#         print("0")
#         func()
#         print("2")
#     return wrapper

# @Decorate
# def Count():
#     print("1")

# Count()

#d) by printing one by one using print function
# def decorate(func):
#     def wrapper(a,b):
#         print("The addition is: ")
#         func(a,b)
#         print("Completed")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(a+b)

# addition(2,2)

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)

# addition(12,12)

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
# addition(12,12)


# def decorate(func):
#     def wrapper(**kwargs):
#         print("\nYour infromation are ---\n")
#         func(**kwargs)
#         print("\n I hope you liked our service\n")
#     return wrapper

# @decorate
# def infromation(**kwargs):
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# infromation(name = "vashu", age = 100, roll_no = 54)
    
# def even_odd(a):
#     print("even") if a%2==0 else print("odd")

# even_odd(0)
# even_odd(2)
# even_odd(12543)

# create list of even number from 1 to 20
# even = []
# odd = []
# for i in range(1,21):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"even numners are: {even}")
# print(f"Odd numbers are : {odd}")

# even = []
# odd = []

# for i in range(1,21):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"Even numbers are: {even}")
# print(f"Odd numbers are: {odd}")

# even = [i for i in range(1,21) if i%2==0]
# print(even)

# even = [i for i in range(1,21) if i%2==0]
# print(even)

# even = []
# odd = []
# for i in range(1,21):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"even numbers: {even}")
# print(f"odd numbers : {odd}")

# even = [i for i in range(1,21) if i%2==0] #list comprehension
# odd = [i for i in range(1,21) if i%2!=0]
# print(f"even number : {even}")
# print(f"odd numbers : {odd}")

# even = [i for i in range(1,21) if i%2==0]
# odd = [i for i in range(1,21) if i%2!=0]
# print(f"Even numbers are: {even}"), print(f"Odd numbers are : {odd}")

# {1 : 1,  2 : 4 ...........}
# squares = {}
# for i in range(1,11):
#     squares [i] = i**2
# print(squares)

# square = {i : i**2 for i in range(1,11)}
# print(squares)

# def add(a,b):
#     print(a+b)

# add = lambda a,b : a+b
# print(add(12,13))
# def add:
#     a = (print("even") if a%2==0 else print("odd"))

# numbers = [1,2,3,4,5,6]
# n = map(lambda n : n*2, numbers)
# print(f" multiplaction of list: ", list(n))

# numbers = [1,2,3,4,5,6]
# n = filter(lambda n : n%2==0, numbers)
# print(f"Even numbers: {list(n)}")

