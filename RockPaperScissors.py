# Two-player Rock-Paper-Scissors game.

__author = "Mohamed Abouelsaadat"

firstPlayer = input("Whats' your name: ")
secondPlayer = input("And your name: ")
p1 = input(firstPlayer + " what would you like to choose rock , paper or scissors ?").lower()
p2 = input(secondPlayer + " what would you like to choose rock , paper or scissors ?").lower()
valid_choices = ('rock','paper','scissors')


def game( p1 , p2):

    if (p1 and p2 not in  valid_choices):
            print("Invalid input!")
    elif p1 == "scissors":
        if p2 == "paper":
            print(firstPlayer + " Wins!")
        else:
            print(secondPlayer + " Wins!")

    elif p1 == "rock":
        if p2 == "scissors":
            print(firstPlayer + " Wins!")
        else:
            print(secondPlayer + " Wins!")

    elif p1 == "paper":
        if p2 == "rock":
            print(firstPlayer + " Wins!")
        else:
            print(secondPlayer + " Wins!")
    elif p1 == p2:
            print("Invalid input!")
            print("It's a draw")

game(p1, p2)