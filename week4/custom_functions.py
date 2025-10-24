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

def sum_weight(weight_of_character, weight_of_inventory):
    total = weight_of_character + weight_of_inventory
    return total
def calc_avg_weight(weight_of_character, weight_of_inventory):
    total = sum_weight(weight_of_character, weight_of_inventory)
    average = total / 2
    return average
def run ():
    character_weight = float(input("weight_of_character: "))
    inventory_weight = float(input("weight_of_inventory: "))

    choice = input('Type "sum" to calculate total weight of character and "average" to calculate average weight of character')
    if choice == "sum":
        total = sum_weight(character_weight, inventory_weight)
        print("f the total weight of character is ", total)
    elif choice == "average":
        average = calc_avg_weight(character_weight, inventory_weight)
        print("f the average weight of character is ", average)
    else:
        print("invalid choice, please type sum or average")


    def display_lower (word):
        print(word.lower())
    def display_upper (word):
        print(word.upper())



























