import random
num = random.randint(1,100)
a = int(input("Guess a number between 1 to 100 : \n"))
c = 1
while(num!=a):
    if(num > a):
        print("Higher Number Please !\n")
    else:
        print("Lower Number please \n")
    a = int(input("Guess a number between 1 to 100 : \n"))
    c = c+1
    
print("Number guessed Correctly !! \n You Won !!")
print(f"You have guessed the number correctly in {c} attempts")
    
