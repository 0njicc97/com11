# import os
#
#
# def cwd():
#     path = os.getcwd()
#     print(f"The current working directory is {path}")
#     print(f"The directory contains the following:")
#     for file in os.listdir(path):
#         print(file)
#
#
# def run():
#     print("Processing...")
#     cwd()
#
#
# if __name__ == "__main__":
#     run()
import csv
#
#
# def display_chars(fle_path,num_chars):
#     with open(fle_path,'r') as csvfile:
#       data = csvfile.read(num_chars)
#       print(data)
#
#
# def display_line(fle_path):
#     with open(fle_path,'r') as csvfile:
#         data = csvfile.readlines()
#         print(data)
#
# def display_text(fle_path):
#     with open(fle_path,'r') as csvfile:
#         data = csvfile.read()
#         print(data)
#
# def run_task2():
#     display_chars("library.txt",5)
#     display_line("library.txt")
#     display_text("library.txt")
#
#
# if __name__ == '__main__':
#     run_task2()


# def search(filename):
#     print("searching...")
#     with open(filename) as file:
#         for location in file:
#             print(f"look in {location.strip()}")
#             print("Done!")
#
# def run_task3():
#     search("library.txt")
#
# if __name__ == "__main__":
#     run_task3()

# def search():
#     print("searching!")
#     sections = ""
#     books =  "Books:\n"
#     with open('file_path') as f:
#         for line in f:
#             if line.startswith(sections):
#                 sections += line
#             else:
#                 books += line
#         print("Done!")
#         return f"{sections}\n\n{books}"
# def save(file_path, data):
#     print("saving!")
#     with open(file_path, 'w') as f:
#         f.write(data)
#     print("Done!")
#
# def run_task4():
#     data = search("books.txt")
#     save("export_books.txt", data)
#
#
# if __name__ == "__main__":
#     run_task4()


import csv


def read(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        print(f"Headings:\n{headings}")

        print("Values:")
        for values in csv_reader:
            print(values)


def run_task1():
    read("clothing.csv")


if __name__ == "__main__":
    run_task1()