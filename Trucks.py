from CsvReader import get_addresses
from CsvReader import get_distances
from CsvReader import get_packages

first_truck_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
second_truck_packages = [3, 6, 18, 25, 36, 38, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 28, 32, 33]
third_truck_packages = [9, 27, 35, 39]

def get_street_address(int):
        return get_packages().get(str(int))[1]

def find_distance(address_x, address_y):
    row = 0
    column = 0

    for address in get_addresses():
        if address[2] == address_x:
            column = int(address[0])
        if address[2] == address_y:
            row = int(address[0])

    return get_distances()[row][column]

def find_best_route(addresses):
    current = ["4001 South 700 East"]
    total_distance = 0.0

    route_distances = list(map((lambda address: find_distance(current[-1],address)), addresses))
    next_index = route_distances.index(min(route_distances))
    next_location = addresses[next_index]
    current.append(next_location)
    total_distance += float(min(route_distances))

    return [route_distances, current, total_distance]

    # for address in addresses:
    #     current_distance = find_distance(current, address)
    #     if current_distance < shortest:
    #         shortest = current

first_truck_route = list(map((lambda package: get_street_address(package)), first_truck_packages))
first_truck_best = find_best_route(first_truck_route)

second_truck_route = []
third_truck_route = []

    # for package in list:
    #     result = map(lambda x: x + x, list)
    #     # return [].append(get_addresses()[package])
    #     return list(result)
