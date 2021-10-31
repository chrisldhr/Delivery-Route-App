from CsvReader import get_packages
from Delivery import first_truck_distances

def convert_str_to_float(time):
    float = 0.0
    (hrs, mins, secs) = time.split(':')
    float += (int(hrs) * 60) + int(mins) + (int(secs) / 60)
    return float

# print(update_package_address(str(9),"410 S State St.", "84111"))
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

def get_status(string_time):
    current_time = convert_str_to_float(string_time)
    total_distance = 0.0

    if current_time >= 620.0:
        update_package_address(str(9),"410 S State St.", "84111")

    statuses = []

    for i in range(1,41):
        statuses.append(get_packages().get(str(i)))

    for status in statuses:
        delivery_time = convert_str_to_float(status[10])
        start_time = convert_str_to_float(status[9])

        if delivery_time <= current_time:
            total_distance += status[8]
            status[11] = "DELIVERED"

        if start_time <= current_time and delivery_time > current_time:
            status[11] = "EN ROUTE"

        # package_id = time[0]
        # delivery_time = convert_str_to_float(time[1])
        # for status in statuses:
        #     if current_time > delivery_time and status[0] == package_id:
        #          statuses[8] = "DELIVERED AT: " + time[1]

    return '\n'.join(map(str,statuses)) + "\nTOTAL DISTANCE: " + str(total_distance.__round__(4)) + " miles"
    # return [statuses[package_id], current_time, delivery_time, package_id]
