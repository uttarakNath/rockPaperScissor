import random
game = 1
score = 0
Cscore =0

print("Some stuff you should know :")
print("We are case-sesitive")
print("you dont need to close the program to end, you can end it any time")
print("score will be displayed only when you end the entire game")
print("thats it! you may now enter the game...")
name = str(input("enter your name here, this will also start the game - "))

while game :
    print("round ",game," begins!")
    user_action = input("Enter a choice (rock, paper, scissor) : ")
    possible_actions = ["rock", "paper", "scissor"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            score = score+1
        else:
            print("Paper covers rock! You lose.")
            Cscore = Cscore+1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            score = score+1
        else:
            print("Scissors cuts paper! You lose.")
            Cscore = Cscore+1
    elif user_action == "scissor":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            score = score+1
        else:
            print("You lose!")
            Cscore = Cscore+1
    else:
        print("your choice is invalid! try again")
        
    
    e = str(input("do you want to continue? 'yes' or 'no'"))
    if e == "no":
        
        print(name+ ", you ended the game in round ",game)
        print(name+"'s score -> ",score)
        print("CPU score ->",Cscore)
        break
    elif e == "yes":
        game = game+1
        continue
    else :
        print("your shoice was invalid. we will take that as a continue")
        


    
