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
from Delivery import first_truck_distances
from Delivery import first_truck_times
from Delivery import first_truck_converted_times

print(get_packages().print())
print(get_packages().get(str(40)))
print(get_addresses())
print(get_distances())
print(first_truck_route)
print(find_distance("195 W Oakland Ave","2010 W 500 S"))
print(first_truck_best)
print(second_truck_best)
print(third_truck_best)
print(first_truck_distances)
print(first_truck_times)
print(first_truck_converted_times)












# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
