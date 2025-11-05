import os
def display_chars(file_path,num_chars):
    with open(file_path,"r") as f:
        under_contents = f.read(num_chars)
        print(under_contents)
display_chars("library.txt",8)


def display_line(file_path):
    with open(file_path,"r") as f:
        lines = f.readline()
        print(lines)
display_line("library.txt")


# def display_text(file_path):
#     with open(file_path,"r") as f:
#         text = f.read()
#         print(text)
# display_text("library.txt")
#
# def run_task2():
#
#     file_path = "library.txt"
#     display_text(file_path)
#     display_chars(file_path,8)
#
#
# if __name__ == "__main__":
#     run_task2()
# #
#
import os
def search(file_path):
    print("searching...")
    sections = ""
    books = "Books:\n"
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("section"):
                sections += line +"\n"
            else:
                books += line + "\n"
                print("Done.!")
            return f"{sections}\n\n{books}"
def save(file_path,data):

    print("saving...")
    with open(file_path,"w") as file:
            file.write(data)
            print("Done.!")
def run_task4():
    file_path = "books.txt"
    data = search(file_path)
    save(file_path,data)
    sections = search(file_path)

if __name__ == "__main__":
    run_task4()


