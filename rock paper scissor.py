from random import randint
import time
play=["rock","paper","scissor"]
computer = play[randint(0,2)]
player = False
while player==False:
    player = input("enter your choice from rock paper and scissor:")
    if(player==computer):
        print("its a tie")
    elif(player=="rock"):
        if(computer=="paper"):
            print("computer's choice",computer)
            time.sleep(2)
            print("You loose , computer Wins")
        else:
            print("computer's choice",computer)
            time.sleep(2)
            print("You Win , Computer looses")
    elif(player=="paper"):
        if(computer=="scissor"):
            print("computer's choice",computer)
            time.sleep(2)
            print("You loose , computer Wins")
        else:
            print("computer's choice",computer)
            time.sleep(2)
            print("You Win , Computer looses")
    elif(player=="scissor"):
        if(computer=="rock"):
            print("computer's choice",computer)
            time.sleep(2)
            print("You loose , computer Wins")
        else:
            print("computer's choice",computer)
            time.sleep(2)
            print("You Win , Computer looses")
    else:
        print("the choice is invalid")
    player=False
    computer = play[randint(0,2)]



        
    
    
