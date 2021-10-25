from HashMap import HashMap
import csv

with open('Data/Packages.csv') as packages_file:
    reader = csv.reader(packages_file, delimiter=',')
    packages = HashMap()

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
        packages.add(id, value)

def get_packages():
    return packages

with open('Data/Addresses.csv') as addresses_file:
    reader = csv.reader(addresses_file, delimiter=',')
    addresses = list(reader)

def get_addresses():
    return addresses

with open('Data/Distances.csv') as distances_file:
    reader = csv.reader(distances_file, delimiter=',')
    distances = list(reader)

def get_distances():
    return distances
