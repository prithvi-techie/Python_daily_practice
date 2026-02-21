# random number guessing game etween 1 to 10

import random
num = random.randint(1,10)
tries = 0


while True:
    guess = int(input("Enter your guess number b/w 1-10: "))
    tries+=1

    if guess == num:
        print(f"You guessed the number in {tries} tries")
        break

    elif num<=guess:
        print("please go a little lower")
    elif num>=guess:
        print("please go a little higher")



    else:
        print("worng guess")