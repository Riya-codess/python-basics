import random
number = random.randint(1,10)
guess = None
while guess!= number:
    guess = int(input("guess the number(1-10): "))
    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
    else:
        print("coreect")
      
