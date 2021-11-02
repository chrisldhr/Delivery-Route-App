# Name: Christopher Liu
# ID: 001274582

from CsvReader import get_packages
from Status import get_status

# The program starts with the module CsvReader.py.
# It loads the data from the csv files in the data folder into a hashmap and lists.
# The hashmap data structure and functions are determined by the module HashMap.py.
# The Trucks.py module then manually loads the packages into the trucks where
# addresses and distances are calculated.
# With those calculations, the nearest neighbor algorithm is used to determine
# the best route for each truck.
# The Delivery.py module determines the times and distance for when the packages
# are delivered, and adds them to the package data in the hashmap.
# The Status.py module takes an input of time and provides the status of the
# packages (at the hub, en route, or delivered).

# User interface for the console command line.
# Allows user to input time and get status of all packages.
# Allows user to get status of single package.
# Space-time complexity: O(1)

def user_interface():
    current_time = ""
    try:
        current_time = input("Please enter a time [hrs:mins:secs] after 08:00:00 to check package status: \n")
        print(get_status(current_time))
    except:
        print("Please enter hours, minutes and seconds in the format of hrs:mins:secs\n")
        exit()

    try:
        package_id = input("Enter a package id to check package status: \n")
        print("Current time: " + current_time)
        print(get_packages().get(str(package_id)))
    except:
        print("Please enter a number between 1 and 40 for the package id\n")
        exit()


user_interface()
