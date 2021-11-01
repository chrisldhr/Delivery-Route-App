# Module that inputs data from csv files in to hash map and lists

from HashMap import HashMap
import csv

# Creation of hash map and insertion of csv data of packages
# Space-time complexity: O(N)
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
        status = '|| AT THE HUB ||'

        value = [id, address, city, state, zip, deadline, size,
            note, status]
        packages.add(id, value)

# Retrieval of hash map data of packages
# Space-time complexity: O(N)
def get_packages():
    return packages

# Insertion of csv data of addresses in to a list
# Space-time complexity: O(N)
with open('Data/Addresses.csv') as addresses_file:
    reader = csv.reader(addresses_file, delimiter=',')
    addresses = list(reader)

# Retrieval of csv data of addresses
# Space-time complexity: O(N)
def get_addresses():
    return addresses

# Insertion of csv data of distances in to a list
# Space-time complexity: O(N)
with open('Data/Distances.csv') as distances_file:
    reader = csv.reader(distances_file, delimiter=',')
    distances = list(reader)

# Retrieval of csv data of distances
# Space-time complexity: O(N)
def get_distances():
    return distances
