import datetime

from Trucks import find_distance
from Trucks import first_truck_best

current_time = 0.0
truck_speed = 18  # miles per hour
first_truck_start = 480.0  # 08:00 in minutes
second_truck_start = 540.16  # 9.10 in minutes???
third_truck_start = 480 + (34 / truck_speed * 60)  # 34 is truck 1 total distance

def distance_traveled(addresses):
    distances = []
    total_distance = 0.0

    for i in range(len(addresses)):
        distance = find_distance(addresses[i], addresses[i - 1])
        total_distance += distance
        distances.append([distance, total_distance])
        # distances.append(distance)
    return distances

def times_delivered(start_time, distances):
    times = []
    for distance in distances:
        time = start_time + ((distance[1] / truck_speed) * 60)
        times.append(time)
    return times

def convert_times(times):
    converted = []
    for time in times:
        convert = str(datetime.timedelta(minutes=time))
        converted.append(convert)
    return converted

first_truck_distances = distance_traveled(first_truck_best)
first_truck_times = times_delivered(first_truck_start, first_truck_distances)
first_truck_converted_times = convert_times(first_truck_times)


