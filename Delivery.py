# Module to calculate delivery times and distances for packages

import datetime
from Trucks import find_distance
from Trucks import first_truck_best
from Trucks import second_truck_best
from Trucks import third_truck_best
from CsvReader import get_packages

truck_speed = 18  # miles per hour
first_truck_start = 480.0  # 08:00 in minutes
second_truck_start = 550.0  # 9.10 in minutes
third_truck_start = 600.0 # 10:00 in minutes

# List of distances traveled between addresses
# Space-time complexity: O(N)
def distance_traveled(addresses):
    distances = []
    total_distance = 0.0

    for i in range(len(addresses)):
        distance = find_distance(addresses[i][1], addresses[i - 1][1])
        total_distance += distance
        distances.append([addresses[i][0], distance, total_distance])
    return distances

# List of delivery times for each package
# Space-time complexity: O(N)
def times_delivered(start_time, distances):
    times = []
    for distance in distances:
        time = start_time + ((distance[2] / truck_speed) * 60)
        times.append([distance[0],time])
    return times

# List of conversions of float time into string time
# Space-time complexity: O(N)
def convert_times(times):
    converted = []
    for time in times:
        convert = str(datetime.timedelta(minutes=time[1]))
        converted.append([time[0],convert])
    return converted

# Insertion of time delivered for a package into hash map
# Space-time complexity: O(1)
def update_package_time(package_id, start_time, time):
    package = get_packages().get(str(package_id))

    id = package[0]
    address = package[1]
    city = package[2]
    state = package[3]
    zip = package[4]
    deadline = package[5]
    size = package[6]
    note = package[7]
    start_time = start_time
    time = time
    status = package[8]

    value = [id, address, city, state, zip, deadline, size,
    note, start_time, time, status]

    get_packages().update(id, value)

# Insertion of distance travelled for a package into hash map
# Space-time complexity: O(1)
def update_package_distance(package_id, new_distance):
    package = get_packages().get(str(package_id))

    id = package[0]
    address = package[1]
    city = package[2]
    state = package[3]
    zip = package[4]
    deadline = package[5]
    size = package[6]
    note = package[7]
    distance = new_distance
    start_time = package[8]
    time = package[9]
    status = package[10]

    value = [id, address, city, state, zip, deadline, size,
    note, distance, start_time, time, status]

    get_packages().update(id, value)

# Conversion of string time to float time
# Space-time complexity: O(1)
def convert_time_to_float(time):
    float = 0.0
    (hrs, mins, secs) = time.split(':')
    float += (int(hrs) * 60) + int(mins) + (int(secs) / 60)
    return float

# Conversion of float time to string time
# Space-time complexity: O(1)
def convert_to_time(float):
    return str(datetime.timedelta(minutes=float))

# Updating packages with added data of delivery time
# Space-time complexity: O(N)
def update_truck_times(start_time,truck_converted_times):
    for time in truck_converted_times:
        package_id = time[0]
        time = time[1]

        if package_id != 0:
            update_package_time(package_id, start_time, time)

# Updating packages with added data of distance travelled
# Space-time complexity: O(N)
def update_truck_distances(truck_distances):
    for distance in truck_distances:
        package_id = distance[0]
        new_distance = distance[1]

        if package_id != 0:
            update_package_distance(package_id, new_distance)

# Creation of lists containing package id, time delivered, distance travelled for each truck
# Insertion of data in to hash map
# Space-time complexity: O(N)
first_truck_distances = distance_traveled(first_truck_best)
first_truck_times = times_delivered(first_truck_start, first_truck_distances)
first_truck_converted_times = convert_times(first_truck_times)
update_truck_times(convert_to_time(first_truck_start), first_truck_converted_times)
update_truck_distances(first_truck_distances)

second_truck_distances = distance_traveled(second_truck_best)
second_truck_times = times_delivered(second_truck_start, second_truck_distances)
second_truck_converted_times = convert_times(second_truck_times)
update_truck_times(convert_to_time(second_truck_start), second_truck_converted_times)
update_truck_distances(second_truck_distances)

third_truck_distances = distance_traveled(third_truck_best)
third_truck_times = times_delivered(third_truck_start, third_truck_distances)
third_truck_converted_times = convert_times(third_truck_times)
update_truck_times(convert_to_time(third_truck_start), third_truck_converted_times)
update_truck_distances(third_truck_distances)
