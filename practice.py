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