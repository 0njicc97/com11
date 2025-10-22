import random

def guess_the_number ():
    print("Please enter the minimum value" )
    minimum_value = int(input())
    print("Please enter the maximum value" )
    maximum_value = int(input())
    secret_number = random.randint(minimum_value, maximum_value)
    print(f"I am thinking of a number between {minimum_value} and {maximum_value} ,can you guess what it is?")
    guess_number = int(input())
    if guess_number < secret_number:
        print("Sorry, you guessed too low,")
        print("try again.")
    elif guess_number > secret_number:
        print("Sorry, you guessed too high,")
        print("try again.")
    elif guess_number == secret_number:
        print("Congratulations, you guessed it!")
guess_the_number()






