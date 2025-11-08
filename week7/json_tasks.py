import json
def read(file_path):
    with open(file_path) as file:
        data = json.load(file)




        print(f'Place Name: {data["location"]}')
        print(f'Place population size: {data["population"]}')


        for data in data['bots']:
            name = data['name']
            stats = data['stats']
            print(f' {name} has the following stats:{stats}.')

def run():
    read("futurama.json")

if __name__ == '__main__':
    run()


