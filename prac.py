# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.balance

# acc = BankAccount(1000)
# acc.deposit(500)
# print(acc.get_balance())   # 1500

# acc.withdraw(2000)         # Insufficient funds
# print(acc.get_balance())   # 1500 (unchanged)

for row in range(6):
    for col in range(7):
        if ((row == 0 and col % 3!=0) or
            (row == 1 and col % 3 == 0) or
            (row - col == 2) or (row + col == 8)):
            print("*", end =" ")

        else:
            print(" ", end = " ")
    print()
