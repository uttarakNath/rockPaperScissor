import random

game=1

while game:

    print(game, " begins!")

    ai=(random.randint(1,3))
    user=str(input("what will you choose:- rock-1, paper-2, scissor-3"))

    if ai==user :
        print("draw!!")

    elif( ai==1 and user==2):
        print("congrats, you win!")

    elif( ai==2 and user==1):
        print("you lose!")

    elif( ai==2 and user==3):
        print("congrats, you win!")

    elif( ai==3 and user==2):        
        print("you lose!")

    elif( ai==3 and user==1):
        print("congrats, you win!")

    elif( ai==1 and user==3):
        print("you lose!")

    game=game+1

    
