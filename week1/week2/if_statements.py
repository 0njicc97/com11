print("enter the type of book?")
book_type = input()
if book_type == "adventure":
    print("I like adventures book!.")
    print("Finished reading book!.")

print("please enter activity to be performed?")
activity = input()
if activity == "calculate":
    print("performing calculations...")
    print("activity completed")
else:
    print("performing activity...")
    print("activity completed")

print("towards which direction should i go,(up,down,left or right)")
direction = input()
if direction == "up":
    print("I will go up...")
elif direction == "down":
    print("I will go down...")
elif direction == "left":
    print("I will go left...")
elif direction == "right":
    print("I will go right...")
else:
    print("not sure which direction should i go")

