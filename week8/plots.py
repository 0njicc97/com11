# import matplotlib.pyplot as plt
#
#
#
# def display_lines(x_values,y_values):
#     plt.plot(x_values,y_values)
#
# def run_task1():
#     x_values = (1,2,3,4,5)
#     y_values = (1,4,9,16,25)
#     display_lines(x_values,y_values)
#     plt.show()
# run_task1()

import matplotlib.pyplot as plt

def small():
    x = [3,4,4,3,3]
    y = [3,3,4,4,3]
    plt.plot(x,y, "ro--")

def medium():
    x = [2,5,5,2,2]
    y = [2,2,5,5,2]
    plt.plot(x,y,"gs--")

def large():
    x = [1,6,6,1,1]
    y = [1,1,6,6,1]
    plt.plot(x,y,"bx-")



small()
medium()
large()
plt.show()