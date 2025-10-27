print("enter the type of book?")
book_type = input()
if book_type == "adventure":
    print("I like adventures book!.")
    print("Finished reading book!.")

print("please enter activity to be performed?")
activity = input()
if activity == "calculate":
    print("performing calculations...")
    print("activity completed")
else:
    print("performing activity...")
    print("activity completed")

print("towards which direction should i go,(up,down,left or right)")
direction = input()
if direction == "up":
    print("I will go up...")
elif direction == "down":
    print("I will go down...")
elif direction == "left":
    print("I will go left...")
elif direction == "right":
    print("I will go right...")
else:
    print("not sure which direction should i go")

print("please enter a whole number?")
number = int(input())
if number % 2 == 0:
    print(f"the number {number} is an even number")
else:
    print(f"the number {number} is an odd number")

print("please entr a first number?")
first_number = int(input())
print("please enter a second number?")
second_number = int(input())
if first_number > second_number:
    print(f"the number {first_number} is greater than the number {second_number}")
elif first_number == second_number:
    print(f"the number {first_number} is equal to the number {second_number}")
else:
    print(f"the number {first_number} is less than the number {second_number}")


print("enter first number?")
first_number = int(input())
print("enter second number?")
second_number = int(input())
print("please enter a third number?")
third_number = int(input())
even_number = 0
odd_number = 0
if first_number % 2 == 0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1
if second_number % 2 == 0:
    odd_number = odd_number + 1
else:
    even_number = even_number + 1
if third_number % 2 == 0:
    odd_number = odd_number + 1
else:
    even_number = even_number + 1

    print(f"there are  {even_number}  even number and {odd_number}  odd number")





