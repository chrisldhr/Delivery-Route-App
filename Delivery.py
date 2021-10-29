import datetime

from Trucks import find_distance
from Trucks import first_truck_best
from Trucks import second_truck_best
from Trucks import third_truck_best
from CsvReader import get_packages

current_time = 0.0
truck_speed = 18  # miles per hour
first_truck_start = 480.0  # 08:00 in minutes
second_truck_start = 550.0  # 9.10 in minutes???
third_truck_start = 600.0 # 10:00 in minutes

def distance_traveled(addresses):
    distances = []
    total_distance = 0.0

    for i in range(len(addresses)):
        distance = find_distance(addresses[i][1], addresses[i - 1][1])
        total_distance += distance
        distances.append([addresses[i][0], distance, total_distance])
        # distances.append(distance)
    return distances

def times_delivered(start_time, distances):
    times = []
    for distance in distances:
        time = start_time + ((distance[2] / truck_speed) * 60)
        times.append([distance[0],time])
    return times

def convert_times(times):
    converted = []
    for time in times:
        convert = str(datetime.timedelta(minutes=time[1]))
        converted.append([time[0],convert])
    return converted

def update_package_address(package_id, new_street, new_zip):
    package = get_packages().get(str(package_id))

    id = package[0]
    address = new_street
    city = package[2]
    state = package[3]
    zip = new_zip
    deadline = package[5]
    size = package[6]
    note = "Address updated"
    status = package[8]

    value = [id, address, city, state, zip, deadline, size,
    note, status]

    get_packages().update(id, value)

def update_package_status(package_id, new_status):
    package = get_packages().get(str(package_id))

    id = package[0]
    address = package[1]
    city = package[2]
    state = package[3]
    zip = package[4]
    deadline = package[5]
    size = package[6]
    note = package[7]
    status = new_status

    value = [id, address, city, state, zip, deadline, size,
    note, status]

    get_packages().update(id, value)

def update_truck_packages(current_time, truck_times):
    for time in truck_times:
        if time[1] < current_time:
            id = time[0]
            new_status = "Delivered at: " + first_truck_converted_times[id][1]
            update_package_status(id, new_status)


first_truck_distances = distance_traveled(first_truck_best)
first_truck_times = times_delivered(first_truck_start, first_truck_distances)
first_truck_converted_times = convert_times(first_truck_times)
first_truck_update = update_truck_packages(740.0, first_truck_times)

second_truck_distances = distance_traveled(second_truck_best)
second_truck_times = times_delivered(second_truck_start, second_truck_distances)
second_truck_converted_times = convert_times(second_truck_times)

third_truck_distances = distance_traveled(third_truck_best)
third_truck_times = times_delivered(third_truck_start, third_truck_distances)
third_truck_converted_times = convert_times(third_truck_times)
