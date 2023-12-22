# rock paper scissors game
import random
gamelist = ["1.ROCK","2.PAPER","3.SCISSORS"]
print("CHOOSE THE OPTION NUMBER")
print(gamelist)
userchoice = int(input("Enter the of your choose: "))
computerchoice = int(random.randint(1,3))
print("Computer choose:",computerchoice)
def resultdisplay():
    if(userchoice == computerchoice):
        print("its is draw")
    elif((userchoice == 1 and computerchoice == 3) or (userchoice == 2 and computerchoice == 1) or (userchoice == 3 and computerchoice == 2)):
        print("I WIN")
    else:
        print("COMPUTER WIN")
result = resultdisplay()
print(result)