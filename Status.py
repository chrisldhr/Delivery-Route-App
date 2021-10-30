from CsvReader import get_packages
from Delivery import first_truck_converted_times

def convert_str_to_float(time):
    float = 0.0
    (hrs, mins, secs) = time.split(':')
    float += (int(hrs) * 60) + int(mins) + (int(secs) / 60)
    return float

def get_status(string_time):
    current_time = convert_str_to_float(string_time)
    statuses = []

    for i in range(1,41):
        statuses.append(get_packages().get(str(i)))

    for time in first_truck_converted_times:
        package_id = time[0]
        delivery_time = convert_str_to_float(time[1])
        for status in statuses:
            if current_time > delivery_time and status[0] == package_id:
                 statuses[8] = "DELIVERED AT: " + time[1]

    return '\n'.join(map(str,statuses))
    # return [statuses[package_id], current_time, delivery_time, package_id]
