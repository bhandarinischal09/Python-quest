import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
a = input("Choose rock, paper or scissors: \n").lower()

while a not in choices:
    print("Invalid choice! Please choose rock, paper or scissors.\n")
    a = input("Choose rock, paper or scissors: \n").lower()
