# Program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("Please choose a number to divide: "))
divisors = []
i = 1

while i < num:
    if (num % i == 0):
        divisors.append(i)
    i = i + 1
print(divisors)
