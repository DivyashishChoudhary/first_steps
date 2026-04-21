import random
secret = random.randint(1,100)
attempts = 0
# This picks a random number between 1 and 100
# Initialized number of attempts at 0

print("Secret number between 1 and 100","\n","Can you guess ?")

while True:
    guess = input("Your guess:")
    attempts +=1

    # Convert the string input to an integer
    guess = int(guess)

    if(guess < secret):
        print("Too low, try again")
    elif(guess > secret):
        print("Too high, try again")
    elif(guess == secret):
        print("You got it!","The no. was",secret)
        print("You took",attempts,"attempt(s)")
        break
    
