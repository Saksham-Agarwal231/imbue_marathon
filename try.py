import random

take = int(input("Enter the maximim no here: "))

yguess = random.randint(1, take)

for n in range(3):
    mguess = int(input("Enter your guess here: "))

    if mguess == yguess:
        print("Kuddos!! your guess is right!!")


    elif yguess > mguess:
        print("Your guess is low!!")


    elif yguess < mguess:
        print("Your guess is high!!")
