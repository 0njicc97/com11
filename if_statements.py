print("what type of book is this?")
book=input()

if book == "adventure":
   print("I Like adventure books!")

print("finished reading the book.")


print("please enter the activity to be performed.")
activity=input()
if activity == "calculations":
    print("calculations")
else: print("performing activity")
print("activity completed!")

print("Towards which direction should i go (up, down, left, or right")
direction =input()
if direction == "up":
    print("i will go up")
elif direction == "down":
    print("i will go down")
elif direction == "left":
    print("i will go left")
elif direction == "right":
    print("i will go right")

print("please enter a whole number")
number=int(input())
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

print("tha car is red.")
car=input()
if car == "red":
    print("the car is red")
else:
    print("the car is not red")
    print("i will like a red car")


print("please enter the first number")
first=int(input())
if first >= 7:
    print("the first number is greater")
    print("please enter the second number")
    second=int(input())
    if second < first:
        print("the second number is smaller")






