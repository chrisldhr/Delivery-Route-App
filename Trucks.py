from CsvReader import get_addresses
from CsvReader import get_distances
from CsvReader import get_packages

first_truck_packages = [1,13,14,15,16,19,20,29,30,31,34,37,40]
second_truck_packages = [3,6,18,25,36,38,2,4,5,7,8,10,11,12,17,21,22,23,24,26,28,32,33]
third_truck_packages = [9,27,35,39]

first_truck_route =[]
second_truck_route =[]
third_truck_route =[]

def find_best_route(list):
    total_distance = 0.0
    shortest = 0.0

def find_distance(x,y):
    address_x = get_packages().get(str(x))[1]
    address_y = get_packages().get(str(y))[1]
    row = 0
    column = 0

    for address in get_addresses():
        if address[2] == address_x:
            row = int(address[0])
        if address[2] == address_y:
            column = int(address[0])

    return[row,column]
    # return get_distances()[int(row)][int(column)]


