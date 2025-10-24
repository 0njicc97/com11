def direction():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps
def run_task1():
    steps = direction()
    for step in range(0, len(steps), 4):
        print(steps)
run_task1()