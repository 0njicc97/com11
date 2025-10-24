#def direction():
#  steps = ["move forward", "move backward", "turn left", "turn right"]
#   return steps


#def run_task1():
    #result = direction()
   # print(result)

#run_task1()


def movement ():
    path = ["move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    print("moving...")
    directions = movement()
    for i in range(0, len(directions), 2):
        print(f"{directions[i]} for {directions[i+1]} steps")

run_task2()


