import random
computerScore=0
userScore=0

print("A game of Rock, Paper, Scissor!!")
print("")
options=["rock","paper","scissor"]

while True:
    userOption=input("Type your move (Rock/Paper/Scissor) or Q to quit: ").lower()
    if userOption=="q":
        break
    if userOption not in options:
        continue 

    computerOption=options[random.randint(0,2)]

    # check user win cases
    if userOption=="rock" and computerOption=="scissor":
        print("You win!")
        userScore+=1
    elif userOption=="paper" and computerOption=="rock":
        print("You win!")
        userScore+=1
    elif userOption=="scissor" and computerOption=="paper":
        print("You win!")
        userScore+=1
    else:
        print("You lose")
        computerScore+=1

print(f"You won {userScore} times.")
print(f"The computer won {computerScore} times.")
print("End of game")
