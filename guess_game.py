import random

print("Hello, What is your name?")
name = input()


print("Well," + name + " I am guessing of number between (1 - 20)")
secretNumber = random.randint(1,20)

for guesstaken in range(1,7):
    print("Take a guess")
    try:
        guess = int(input())

        if guess < secretNumber:
            print("Your guess is too low.")
        elif guess > secretNumber:
            print("Your guess is too high.")
        else:
            break # user guessed correctly
    except Exception as e:
        print("Invalid ! Kindly enter an integer")

if guess == secretNumber:
    print("Good job" + name + "you have guessed it in " + str(guesstaken) +" numbers")
else:
    print("Nope ! The number i was thinking of was " + str(secretNumber))


