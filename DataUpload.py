from HashMap import HashMap
import csv

hash_map = HashMap()

with open('packages.csv') as file:
    reader = csv.reader(file, delimiter=',')

    for row in reader:
        hash_map.add(int(row[0]), row)

def get_hash_map():
    return hash_map


