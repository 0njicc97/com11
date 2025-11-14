import csv


records = []

headings = []

def load_data(file_path):
    print("Loading data...")
    with open(file_path) as file:
        reader = csv.reader(file)
        headers = next(reader)
        for line in reader:
            records.append(line)
            print("Done")
def display_menu():
    print(
        """
        please select one of the following options:
        [1] Display the names of all passengers
        [2] Display the numbers of passengers that survive
        [3] Display the number of passengers per gender
        [4] Display the number of passengers per age group
        [5] Display the number of survivors per age group""")


    return int(input())


def display_passenger_names():
    print("The names of the passengers are....\n")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)

def display_num_survivors():
    num_survivors = 0
    for record in records:
        survivors_status = int(record[1])
        if survivors_status == 1:
            num_survivors += 1
            print(f"{num_survivors} passengers survived")

def display_passengers_per_gender():
    females = 0
    males = 0
    for record in records:
     gender = record[4]

     if gender.lower() == "male":
        males += 1

     else:
         females += 1
         print(f"{females} males:{males}")

def run():
    file = "titanic (1) (3).csv"
    load_data(file)
    display_menu()
    display_passenger_names()
    display_num_survivors()
    display_passengers_per_gender()

    if __name__ == "__main__":
     run()














