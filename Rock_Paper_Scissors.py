# gaming with python rock paper scissors 
#using multiple condition and logical operator
#using input as well to collect data from the user
#and compera with the one computer gave us them
#print the answer for the user as well


import random   #---> and also imported random module and the proparetice
                 #---> randint that is all for now


COMPUTER  =  random.randint(0, 2)
USER  =  int(input("What is your choice? : choose 0 for Rock, 1 for Paper, 2 for Scissors :\n"))


if USER > 2 or  USER  < 0:
    print("You typin in an invalid number Computer win's")
elif  COMPUTER == USER:
    print("It's a draw")
elif COMPUTER == 2 and USER == 0:
    print("You win")
elif USER == 2 and  COMPUTER == 0:
    print("You lose")
elif COMPUTER > USER:
    print("You lose")
elif  USER  >  COMPUTER:
    print("You win")

print(f"Computer chose : {COMPUTER}")
