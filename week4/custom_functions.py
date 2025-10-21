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








