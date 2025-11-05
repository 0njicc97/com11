import csv
with open("library.txt", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        heading = row[0]
        print(heading)
