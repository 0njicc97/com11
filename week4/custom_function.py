
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