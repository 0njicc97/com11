def direction():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps
def run_task1():
    steps = direction()
    for step in range(0, len(steps), 4):
        print(steps)
run_task1()

def movement():
    path = ( "Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1)
    return path
def run_task2():
    print("moving...")
    path = movement()
    for step in range(0, 1,len(path) ):
        print(f"{path}[i] for {path} for {step}")
run_task2()




def directions():
    steps = ("Move Forward", "Move Backward", "Turn Left" "Turn Right")
    return steps
def menu():
    print("please select a direction:")
    choice = direction()
    for i in range(0,len(choice),):
        print(f"{i}: {choice[i]} ")
menu()





