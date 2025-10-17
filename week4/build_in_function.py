print("program started!")
print("please enter a standard character")
character = input()

if len(character) == 1:
    ASCII = ord(character)
    print(f"The ASCII code for {character} is {ASCII}")
else:
    print("enter a single latter")

print("program ended")

print("program started!")
print("Please enter an ASCII code:")
ASCII_code = int(input())
if ASCII_code in range (32,127):
    print("The ASCII code for {character} is {ASCII}")




















