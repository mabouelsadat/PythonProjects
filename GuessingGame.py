#Program generates a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tells them whether they guessed too low, too high, or exactly right.
__author = "Mohamed Abouelsaadat"

import random

number = random.randint(1, 9)
count = 0

guess = int(input("What's your guess: "))
while guess != number and guess != "exit":
    if guess != number:
        if guess < number:
            print("Too low")
            guess = int(input("What's your guess: "))
            count +=1
        elif guess > number:
            print("Too high")
            guess = int(input("What's your guess: "))
            count += 1
else:
    print("You got it" + " in " + str(count) + " times")


