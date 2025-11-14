import csv


def started(msg =""):
    with open('file_path','r') as file:
        msg = csv.reader(file)

        print('------------------')
        print(f'operation started:reading data from {msg}..\n')
    

def complete():
    print('------------------:operation completed')

def error(msg):
    print(f'error: {msg}')



def menu():
    print('select one of the following options:')
    print('[years]  List unique years')
    print('[tally] Tally up medals')
    print('[C tally] Tally Tally up medals for each team')
    print('[exit] Exit the program')
    option = input('Enter your choice: ')
    return option
def display_medal_tally(tally):
    for key,values in tally:
        print(f'{key},{values}')

def run():
    file_path = 'athlete_events.csv'
    menu()
    complete()

run()


