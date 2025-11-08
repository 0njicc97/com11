# import json
# def read(file_path):
#     with open(file_path) as file:
#         data = json.load(file)
#
#
#
#
#         print(f'Place Name: {data["location"]}')
#         print(f'Place population size: {data["population"]}')
#
#
#         for data in data['bots']:
#             name = data['name']
#             stats = data['stats']
#             print(f' {name} has the following stats:{stats}.')
#
# def run():
#     read("futurama.json")
#
# if __name__ == '__main__':
#     run()

import json


def read_task2(file_path):
    print("reading..")

    with open(file_path,'r') as file:
        data = json.load(file)

    print("Done!")

    return data

def save(file_path, data):
    print("Exporting...")

    with open(file_path,'w') as file:
        json.dump(data, file, indent=2)
    print("Done!")

def run_tasks2():
    jason_data = read_task2('futurama.json')
    save(jason_data,jason_data)

if __name__ == '__main__':
    run_tasks2()
