from HashMap import HashMap
import csv

hash_map = HashMap()


with open('Data/Packages.csv') as file:
    reader = csv.reader(file, delimiter=',')

    for row in reader:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        size = row[6]
        note = row[7]
        status = 'At the hub'

        value = [id, address, city, state, zip, deadline, size,
            note, status]
        hash_map.add(id, value)

def get_packages():
    return hash_map




