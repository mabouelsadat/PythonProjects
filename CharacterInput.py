while(True):

    name = input("Enter your name: ")
    age = input("Enter your age(Max 100 years old): ")
    # Checking that name and age not empty and age is less than 100 years old
    if (len(name) == 0 or len(age) == 0 or int(age) >= 100):
        print("Please enter valid data")
        continue
    else:
        calage = 100 - int(age)
        print("Hi " + name + " you are " + str(age) + " However you will turn 100 years old after " + str(
            calage) + " years ENJOY!!!")
    break