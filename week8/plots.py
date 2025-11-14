import matplotlib.pyplot as plt
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

# import matplotlib.pyplot as plt
#
# def small():
#     x = [3,4,4,3,3]
#     y = [3,3,4,4,3]
#     plt.plot(x,y, "ro--")
#
# def medium():
#     x = [2,5,5,2,2]
#     y = [2,2,5,5,2]
#     plt.plot(x,y,"gs--")
#
# def large():
#     x = [1,6,6,1,1]
#     y = [1,1,6,6,1]
#     plt.plot(x,y,"bx-")
#
#
#
# small()
# medium()
# large()
#plt.show()

def coordinate():
    print("please enter and x_values")
    x_values = input()
    print("please enter and y_values")
    y_values = input()
    return x_values, y_values

def path():
    print("retrieving path..")
    x_values = []
    y_values = []
    for i in range(4):
        data = coordinate()
        x,y = data
        x_values.append(x)
        y_values.append(y)
    return [x_values, y_values]
def run_task3():
    values = path()
    plt.plot(values[0], values[1], 'r--o')
    plt.show()
run_task3()







