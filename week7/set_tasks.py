# def observe():
#
#      observations = {"car","sky scrapper","sky scrapper","bike","house","house"}
#
#
#      return observations
#
# def run_task1():
#
#     items = observe()
#
#     print(items)
#
#
#
# run_task1()
#


def observed_items():
    observations = []
    for i in range(7):
        user_input = input("Enter observation: ")
        observations.append(user_input)
    return observations

def run_task2():
    print("counting observations...")
    observations = observed_items()
    items = set()
    for i in observations:
        counts = (i,observations.count(i))
        items.add(counts)

    print(items)

run_task2()








