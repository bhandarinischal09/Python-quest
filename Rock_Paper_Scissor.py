import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
a = input("Choose rock, paper or scissors: \n").lower()

while a not in choices:
    print("Invalid choice! Please choose rock, paper or scissors.\n")
    a = input("Choose rock, paper or scissors: \n").lower()
print("Computer chooses:", computer)

if a == computer:
    print("It's a Draw!")

elif a == "rock":
    if computer == "scissors":
        print("You Won!")
    else:
        print("Computer Won!")

elif a == "paper":
    if computer == "rock":
        print("You Won!")
    else:
        print("Computer Won!")

elif a == "scissors":
    if computer == "paper":
        print("You Won!")
    else:
        print("Computer Won!")