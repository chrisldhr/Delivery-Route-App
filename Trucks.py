# Module that manually loads packages into truck and calculates best route

from CsvReader import get_addresses
from CsvReader import get_distances
from CsvReader import get_packages

# Load packages into trucks
# Space complexity: O(N)
# Time complexity: O(1)
first_truck_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
second_truck_packages = [3, 6, 18, 36, 38, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 28, 32, 33]
third_truck_packages = [9, 25, 27, 35, 39]

# Retrieval of street address
# Space: O(1)
# Time complexity: O(N)
def get_street_address(int):
    return get_packages().get(str(int))[1]

# Calculation of distance between two addresses
# Space-time complexity: O(N)
def find_distance(address_x, address_y):
    row = 0
    column = 0

    for address in get_addresses():
        if address[2] == address_x:
            column = int(address[0])
        if address[2] == address_y:
            row = int(address[0])

    if get_distances()[row][column] == "":
        distance = get_distances()[column][row]
    else:
        distance = get_distances()[row][column]

    return float(distance)

# The core algorithm that uses the nearest neighbor algorithm to determine the best route.
# It first calculates the distances from the hub.
# The closest address with the smallest distance then gets added to the best route.
# Then new distances are calculated from that added address.
# The algorithm completes when no packages are left and returns the truck back to the hub.
# Space-time complexity: O(N^2)
def find_best_route(addresses):
    hub = [0,"4001 South 700 East"]
    best_route = [hub]
    total_distance = 0.0

    while True:
        route_distances = list(map((lambda address: find_distance(best_route[-1][1], address[1])), addresses))
        shortest_distance = min(route_distances)
        next_closest_index = route_distances.index(shortest_distance)
        next_closest_address = addresses[next_closest_index]
        best_route.append(next_closest_address)
        total_distance += shortest_distance
        addresses.pop(next_closest_index)
        if len(addresses) == 0:
            total_distance += find_distance(best_route[-1], hub)
            best_route.append(hub)
            break

    return best_route

# Creation of lists containing package id and associated street address for each truck
# Space-time complexity: O(N)
first_truck_route = list(map((lambda package: [package, get_street_address(package)]), first_truck_packages))
second_truck_route = list(map((lambda package: [package, get_street_address(package)]), second_truck_packages))
third_truck_route = list(map((lambda package: [package, get_street_address(package)]), third_truck_packages))

# Creation of lists containing addresses of best route for each truck
# Space-time complexity: O(N)
first_truck_best = find_best_route(first_truck_route)
second_truck_best = find_best_route(second_truck_route)
third_truck_best = find_best_route(third_truck_route)


