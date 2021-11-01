# Module to update wrong address and create a list of statuses for packages

from CsvReader import get_packages
from Delivery import first_truck_distances

# Conversion of string time to float time
# Space-time complexity: O(1)
def convert_str_to_float(time):
    float = 0.0
    (hrs, mins, secs) = time.split(':')
    float += (int(hrs) * 60) + int(mins) + (int(secs) / 60)
    return float

# Update of package address
# Space-time complexity: O(1)
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
    distance = package[8]
    start_time = package[9]
    time = package[10]
    status = package[11]

    value = [id, address, city, state, zip, deadline, size,
             note, distance, start_time, time, status]

    get_packages().update(id, value)

# Creation of list of statuses for all packages
# Space-time complexity: O(N)
def get_status(string_time):
    current_time = convert_str_to_float(string_time)
    total_distance = 0.0

    if current_time >= 620.0:
        update_package_address(str(9), "410 S State St.", "84111")

    statuses = []

    for i in range(1, 41):
        statuses.append(get_packages().get(str(i)))

    for status in statuses:
        delivery_time = convert_str_to_float(status[10])
        start_time = convert_str_to_float(status[9])

        if delivery_time <= current_time:
            total_distance += status[8]
            status[11] = "|| DELIVERED AT: " + status[10] + " ||"

        if start_time <= current_time and delivery_time > current_time:
            status[11] = "|| EN ROUTE ||"

    return '\n'.join(map(str, statuses)) + "\n\nTOTAL DISTANCE: " + str(total_distance.__round__(4)) + " miles\n"
