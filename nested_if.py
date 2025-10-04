print("enter the cover type ( hard or soft ) of the book.")
book_type = input()
if book_type == "soft_cover":
    print("soft cover, perfect bounds book are very popular!")
    print("soft covers with coils or stitches are great for short books")
else:
    if book_type == "hard_cover":
        print("books with har covers can be more expensive!")


print("where should I look?")
look=input()
if look == "in_the_bedroom":
    print("where in the bedroom should I look?")
    if look == "in_the_cupboard":
        print("found some mess but no phone.")
elif look == "in the living room":
    print("where in the living room should I look?")
    if look == "on the table":
        print("yes! found my phone")
    else:
        print("found some stuffs but no phone.")







