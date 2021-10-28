import datetime

from Trucks import find_distance
from Trucks import first_truck_best
from Trucks import second_truck_best
from Trucks import third_truck_best

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

first_truck_distances = distance_traveled(first_truck_best)
first_truck_times = times_delivered(first_truck_start, first_truck_distances)
first_truck_converted_times = convert_times(first_truck_times)

second_truck_distances = distance_traveled(second_truck_best)
second_truck_times = times_delivered(second_truck_start, second_truck_distances)
second_truck_converted_times = convert_times(second_truck_times)

third_truck_distances = distance_traveled(third_truck_best)
third_truck_times = times_delivered(third_truck_start, third_truck_distances)
third_truck_converted_times = convert_times(third_truck_times)
