import random

take = int(input("Enter the maximim no here: "))

yguess = random.randint(1, take)

for n in range(3):
    
     try:
       mguess = int(input("Enter your guess here: "))


     except:
        print("Your guess is not a number!!!")
        mguess = int(input("Enter your guess here:"))


     if mguess == yguess:
        print("Kuddos!! your guess is right!!")
        break


     elif yguess > mguess:
        print("Your guess is low!!")


     elif yguess < mguess:
        print("Your guess is high!!")
    

    
