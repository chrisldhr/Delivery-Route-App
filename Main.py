# Name: Christopher Liu
# ID: 001274582

from CsvReader import get_packages
from Status import get_status

# User interface for the command line in the console.
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
