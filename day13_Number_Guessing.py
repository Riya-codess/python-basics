# importing random module to generate random numbers
import random
number = random.randint(1,10)
guess = None
# Loop will run until user guesses the correct number
while guess!= number:
    guess = int(input("guess the number(1-10): "))
    
    # Checking if guess is lower, higher, or correct
    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
    else:
        print("coreect")
      
