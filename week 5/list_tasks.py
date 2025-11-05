# def direction():
#  steps = ["move forward", "move backward", "turn left", "turn right"]
#  return steps
#
# def run_task1():
#     result = direction()
#     print(result)
#
# run_task1()
from week4.custom_function import steps_remaining


# # def movement ():
# #    path = ["move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
# #    return path
# #
# #
# #
# def run_task2():
#     print("moving...")
#     directions = movement()
#     for i in range(0, len(directions), 2):
#         print(f"{directions[i]} for {directions[i+1]} steps")

# run_task2()
# #
# def directions():
#    steps = ["move forward","move backward","Turn left","Turn right",]
#    return steps
#
# def menu():
#      print("please select a direction:")
#      direction = directions()
#      for i in range(len(direction)):
#       print(f"{i}: {direction[i]}")
# menu()
# #
def directions():
 steps = ["move forward", "move backward", "turn left", "turn right"]
 return steps
def menu_and_input():
    print("please select a direction:")

    direction = directions()

    for index in range(0,len(direction),):
        print(f"{index}: {direction} ")

    choice = input("enter your choice: ")
    return choice

def run_task4():
    route = []
    print("working out escape route")
    for index in range(5):
        route.append(menu_and_input())
        print(f"Escape route: {route[index]}")
run_task4()















