import os


def cwd():
    path = os.getcwd()

    print(f"current working Directory is: {path}")
    print("The Directory contains of the following files:")
    for file in os.listdir(path):
        print(file)
cwd()
