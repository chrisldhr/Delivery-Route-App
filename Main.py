#Name: Christopher Liu
#ID: 001274582

from HashMap import HashMap
from CsvReader import get_packages
from CsvReader import get_addresses
from CsvReader import get_distances
from Trucks import find_distance
from Trucks import first_truck_route
from Trucks import first_truck_best
from Trucks import second_truck_best
from Trucks import third_truck_best
from Delivery import first_truck_distances, second_truck_times, third_truck_times, first_truck_update
from Delivery import first_truck_times
from Delivery import first_truck_converted_times
from Delivery import second_truck_converted_times
from Delivery import third_truck_converted_times
from Delivery import update_package_address

print(get_packages().print())
print(get_packages().get(str(40)))
print(get_addresses())
print(get_distances())
print(first_truck_route)
print(find_distance("195 W Oakland Ave","2010 W 500 S"))
print(first_truck_best)
print(second_truck_best)
print(third_truck_best)
print(get_packages().print())
print(update_package_address(str(9),"410 S State St.", "84111"))
print(get_packages().print())
print(first_truck_distances)
print(first_truck_times)
print(second_truck_times)
print(third_truck_times)
print(first_truck_converted_times)
print(second_truck_converted_times)
print(third_truck_converted_times)
first_truck_update
print(get_packages().print())


