# Project 1 Snake Water Gun Game 
import random
computer = random.choice([-1, 0, 1])
youstr = input("Emter your choice: ")
youDict = {"s": 1, "w": -1,"g": 0} 
you = youDict[youstr]

if(computer == you):
    print("Draw!")

else:
    if(computer == -1 and you == 1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You Lose!")

    elif(computer == 0 and you == -1):
        print("You Lose!")

    elif(computer == 0 and you == 0):
        print("You Win!")

    else:
        print("Something went wrong!")


