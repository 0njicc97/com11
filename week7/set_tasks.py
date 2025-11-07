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

#
# def observed_items():
#     observations = []
#     for i in range(7):
#         user_input = input("Enter observation: ")
#         observations.append(user_input)
#     return observations
#
# def run_task2():
#     print("counting observations...")
#     observations = observed_items()
#     items = set()
#     for i in observations:
#         counts = (i,observations.count(i))
#         items.add(counts)
#
#     print(items)
#
# run_task2()
#
#
#
#
#

# def observe_items():
#     observation = []
#     for i in range(5):
#         user = input("enter values")
#         observation.append(user)
#     return observation
# def remove_observations(observation):
#     print("Do you wish to remove observations?")
#     answer = input("yes/no")
#     while answer == "yes":
#         print("enter a string representing observation to be removed")
#         respond = input()
#         observation.remove(respond)
#         print("Do you wish to remove observations?")
#         answer = input("yes/no")
#
#     return observation
#
# def run_task3():
#     observation = observe_items()
#     removed=remove_observations(observation)
#     print(removed)
# run_task3()
#
#











