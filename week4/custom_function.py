
def escape_by ():
 plan = input("enter a plan: ")
 if plan == "jumping over":
  print("we cannot escape that way!The boulder is too big")
 elif plan == "running around":
  print("we cannot escape that way!The boulder is moving fast")
 elif plan == "cross bridge":
  print("That might just work!lets go")
 else: print("we cannot escape that way! The boulder is on the way")

 escape_by()


def cross_bridge():
 print("cross steps")
cross_steps =input("how many cross steps?")
if cross_steps > "5":
 print("the bridge is collapsing")
elif cross_steps < "5":
 print("we most keep going")
cross_bridge()

def cross_bridge():
 print("climb_ladder")
steps_remaining = input("how many steps remain?")
steps_crossed = input("how many steps crossed?")
if steps_remaining < steps_crossed:
 print("still a long way to go")
elif steps_remaining > steps_crossed:
 print("we almost there")
cross_bridge()


def display_ladders(steps):
 print("ASCII_ladder, + steps")
steps_remaining = input("how many steps remain?")
def create_ladder():
 print("number of steps")
number_of_steps = input("how many steps?")
display_ladders(number_of_steps)
create_ladder()

def some_weight():
 return weight_of_character + weight_of_person
weight_of_character =input()
weight_of_person = input()

def calc_avg_weight():
 return weight_of_character +weight_of_person
some_weight()

def run():
