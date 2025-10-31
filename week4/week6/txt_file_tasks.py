# import os
#
#
# def cwd():
#     path = os.getcwd()
#
#     print(f"current working Directory is: {path}")
#     print("The Directory contains of the following files:")
#     for file in os.listdir(path):
#         print(file)
#
# cwd()

# def display_chars(file_path,num_chars):
#     with open(file_path,"r") as f:
#         under_contents = f.read(num_chars)
#         print(under_contents)
# display_chars("library.txt",8)
#
#
# def display_line(file_path):
#     with open(file_path,"r") as f:
#         lines = f.readline()
#         print(lines)
# display_line("library.txt")


# def display_text(file_path):
#     with open(file_path,"r") as f:
#         text = f.read()
#         print(text)
# display_text("library.txt")
#
# def run_task2():
#     """run all diplay function on library text"""
#     file_path = "library.txt"
#     display_text(file_path)
#     display_chars(file_path,8)
#
#
# if __name__ == "__main__":
#     run_task2()


def search(file_name):
    print("searching...")
    with open(file_name,"r") as f:
        lines = f.readlines()
        for line in lines:
            print(f"looking in {line.strip()}")
        print("Done!")

def run_task3():
    search("library.txt")
run_task3()
