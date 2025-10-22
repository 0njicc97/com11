#def listen ():
    #print("please enter a word representing a sound")
    #word = input()
    #print(f"That was loud  {word}")
#listen()


def identity ():
    print("please enter a word representing what you see?")
    word = input()
    if word == "a_large_boulder":
        print("it is time to run!")
    else:
        print("we will be fine.")
    identity()

def escape_by(plan):
    if plan == "jumping over":
        print("we cannot escape that way! The Boulder is too big!")
    if plan == "Running around":
        print("We cannot escape that way! The Boulder is moving too fast")
    if plan == "cross bridge":
        print("That might just work!Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way")
    escape_by("jumping over")


def cross_bridge (steps):
    print("cross steps")
    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We most keep going")
    cross_bridge(4)
    cross_bridge(3)
    cross_bridge(2)
    cross_bridge(1)

def display_ladder (steps):
    print(f"Ascii ladder {steps}")
def create_ladder ():
    steps = input("How many steps would you like?")
display_ladder(8)
create_ladder()
display_ladder(8)
create_ladder()
display_ladder(8)















