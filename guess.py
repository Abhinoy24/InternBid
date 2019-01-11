import random
a = random.randint(1, 9)
guess = 0

while guess !=a and guess != "exit":
    guess = input("enter your guess:")
    
    if guess == "exit":
        break

    guess = int(guess)

    if guess < a:
        print("Your guess is too low")
    elif guess > a:
        print("Your guess is too high")
    else:
        print("Your guess matched")
