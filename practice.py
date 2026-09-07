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