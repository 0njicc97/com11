print("whats is your name?")
name = input()
print(f"It is nice to meet you  {name}")

name = input("whats is your name?")
print(f"It is nice to meet you  {name}")



print("please enter a character for the eye")
eye = input()
print("########")
print("#      #")
print("########")
print("your age is?")
user_age = input()
print(f"your age is {user_age}")


print("enter your name")
name = input()
print("enter your age,in years")
age = int(input())
print("enter your weight, in kilograms")
weight = float(input())
print(f"your name is {name}, your age is {age},  your weight is {weight}")

# Read in data
print("Please enter number of lives")
lives = int(input())

print("Please enter energy level")
energy = int(input())

print("Please enter shield level")
shield = int(input())

# Display bot data
print(f"Lives:  {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")