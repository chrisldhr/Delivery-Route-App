#Name: Christopher Liu
#ID: 001274582

from HashMap import HashMap
from CsvReader import get_packages
from CsvReader import get_addresses
from CsvReader import get_distances
from Trucks import find_distance

# With self.size = 40, pacakage 40 doesn't load?
print(get_packages().print())
print(get_packages().get(str(40)))
print(get_addresses())
print(get_distances())
print(find_distance(1,2))

# h = HashMap()
# h.add('Bob', '567-8888')
# h.add('Ming', '293-6753')
# h.add('Ming', '333-8233')
# h.add('Ankit', '293-8625')
# h.add('Aditya', '852-6551')
# h.add('Alicia', '632-4123')
# h.add('Mike', '567-2188')
# h.add('Aditya', '777-8888')
# h.print()
# h.delete('Bob')
# h.print()
# print('Ming: ' + h.get('Ming'))
# print(h.keys())












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
