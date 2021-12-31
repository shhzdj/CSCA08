"""CSC108/A08: Fall 2020 -- Assignment 2: Rent-a-bike

This code is provided solely for the personal and private use of
students taking the CSC108 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve,
Diane Horton, Michael Liut, Jacqueline Smith, and Anya Tafliovich.

"""

import copy
import math
from typing import List, TextIO

from constants import (ID, NAME, LATITUDE, LONGITUDE, CAPACITY,
                       BIKES_AVAILABLE, DOCKS_AVAILABLE, IS_RENTING,
                       IS_RETURNING, NO_KIOSK_LABEL, EARTH_RADIUS,
                       SOUTH, NORTH, EAST, WEST, DIRECTIONS)


'''For simplicity, we'll use "Station" in our type contracts to
indicate that we mean a list containing station data.

You can read "Station" in a type contract as:
List of: int, str, float, float, int, int, int, bool, bool

where the values at each index represent the station data as described
in the handout.
'''

# Sample data for use in docstring examples
SAMPLE_STATIONS = [
    [7090, 'Danforth Ave / Lamb Ave',
     43.681991, -79.329455, 15, 4, 10, True, True],
    [7486, 'Gerrard St E / Ted Reeve Dr',
     43.684261, -79.299332, 22, 5, 17, False, False],
    [7571, 'Highfield Rd / Gerrard St E - SMART',
     43.671685, -79.325176, 19, 14, 5, True, True]]
HANDOUT_STATIONS = [
    [7000, 'Ft. York / Capreol Crt.',
     43.639832, -79.395954, 31, 20, 11, True, True],
    [7001, 'Lower Jarvis St / The Esplanade',
     43.647992, -79.370907, 15, 5, 10, True, True]]
FAKE_STATIONS = [
    [1000, 'Street Ave / Road Ave',
     43.0, -79.3, 20, 0, 20, True, True],
    [1001, 'Street Ave / Road Ave',
     43.0, -79.4, 20, 20, 0, True, True],
    [1002, 'Street Ave / Road Ave - SMART',
     43.1, -79.3, 20, 20, 0, True, True],
    [1003, 'Street Ave / Road Ave',
     42.9, -79.3, 20, 10, 10, True, True]]
MY_STATIONS = [
    [100, 'station 100', -40, 80, 12, 1, 2, True, True],
    [101, 'station 101', 20, 35, 20, 0, 20, False, False],
    [103, 'station 103', 20, 70, 10, 3, 9, True, True],
    [104, 'station 104 - SMART', -50, 80, 10, 22, 7, False, False]]

# Used in docstring examples to avoid using == with floats.
EPSILON = 0.01

#################### BEGIN HELPER FUNCTIONS ####################


def is_number(value: str) -> bool:
    """Return True if and only if value represents a decimal number.

    >>> is_number('csca108')
    False
    >>> is_number('  098 ')
    True
    >>> is_number('+3.14159')
    True

    """
    return value.strip().lstrip('-+').replace('.', '', 1).isnumeric()


def is_integer(value: str) -> bool:
    """Return True if and only if value represents an integer.

    >>> is_integer('+2108')
    True
    >>> is_integer('  765 ')
    True
    >>> is_integer('-4.1236')
    False

    """
    return value.strip().lstrip('-+').isdigit()


def true_or_false(data: str) -> bool:
    """Return True of string data is true, False otherwise. Cases are ignored.

    precondition: data can only be 'true' or 'false'.

    >>> true_or_false('true')
    True
    >>> true_or_false('True')
    True
    >>> true_or_false('FaLsE')
    False

    """
    if data.lower() == 'true':
        return True
    return False


def float_or_int(value: float) -> object:
    """Return a float value if the given value is a decimal, and
    return an integer value of the given value is a whole number

    precondition: value should be numberic.

    >>> float_or_int('3.2')
    3.2
    >>> float_or_int('2.0')
    2
    >>> float_or_int('4.0')
    4

    """
    value = float(value)
    if value == int(value):
        return int(value)
    return float(value)


def get_long_and_lat(station_id: int, stations: List['Station']) -> list:
    """Return the longitude and latitude of a station form stations
    according to the station_id.

    >>> get_long_and_lat(1000, FAKE_STATIONS)
    [-79.3, 43.0]
    >>> get_long_and_lat(7001, HANDOUT_STATIONS)
    [-79.370907, 43.647992]
    >>> get_long_and_lat(7571, SAMPLE_STATIONS)
    [-79.325176, 43.671685]

    """
    new_list = []
    for station in stations:
        if station[ID] == station_id:
            new_list = [station[LONGITUDE], station[LATITUDE]]
    return new_list


def get_distance(lat1: float, lon1: float,
                 lat2: float, lon2: float) -> float:
    """Return the distance in kilometers between the two locations defined
    by (lat1, lon1) and (lat2, lon2), rounded to the nearest metre.
    >>> answer = get_distance(43.659777, -79.397383, 43.657129, -79.399439)
    >>> abs(answer - 0.338) < EPSILON
    True
    >>> answer = get_distance(43.67, -79.37, 55.15, -118.8)
    >>> abs(answer - 3072.872) < EPSILON
    True

    """
    # This function uses the haversine function to find the distance
    # between two locations. You do NOT need to understand why it
    # works.  You will just need to call on the function and work with
    # what it returns.  Based on code at goo.gl/JrPG4j
    lon1, lat1, lon2, lat2 = (math.radians(lon1), math.radians(lat1),
                              math.radians(lon2), math.radians(lat2))
    lon_diff, lat_diff = lon2 - lon1, lat2 - lat1

    a_value = (math.sin(lat_diff / 2) ** 2 +
               math.cos(lat1) * math.cos(lat2) * math.sin(lon_diff / 2) ** 2)
    c_value = 2 * math.asin(math.sqrt(a_value))

    return round(c_value * EARTH_RADIUS, 3)


# It isn't necessary to call this function to implement your bikes.py
# functions, but you can use it to create larger lists for testing.
# See the main block below for an example of how to do that.
def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    """Return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of
    csv_file.

    Docstring examples not given since results depend on data to be
    input.

    """
    csv_file.readline()  # read and discard header

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data

#################### END HELPER FUNCTIONS ####################


# Note: you will most certainly need more examples to test your
# functions!

def clean_data(data: List[List[str]]) -> None:
    """Replace each string in all sublists of data as follows: replace
    with
    - an int iff it represents a whole number,
    - a float iff it represents a number that is not a whole number,
    - True iff it is 'True' (case-insensitive),
    - False iff it is 'False' (case-insensitive),
    - None iff it is 'null' or the empty string.

    >>> data = [['abc', '123', '45.6', 'true', 'False']]
    >>> clean_data(data)
    >>> data
    [['abc', 123, 45.6, True, False]]
    >>> data = [['ab2'], ['-123'], ['FALSE', '3.2'], ['3.0', '+4', '-5.0']]
    >>> clean_data(data)
    >>> data
    [['ab2'], [-123], [False, 3.2], [3, 4, -5]]
    >>> data = [['-13.5', ''],['+2002', 'hello', 'True', 'Null']]
    >>> clean_data(data)
    >>> data
    [[-13.5, None], [2002, 'hello', True, None]]

    """
    for item in data:
        for j in range(len(item)):
            if item[j].lower() in ['true', 'false']:
                item[j] = true_or_false(item[j])
            elif is_number(item[j]):
                item[j] = float_or_int(item[j])
            elif item[j] in ['', 'Null']:
                item[j] = None


def has_kiosk(station: 'Station') -> bool:
    """Return True if and only if the given station has a kiosk.

    >>> has_kiosk(SAMPLE_STATIONS[0])
    True
    >>> has_kiosk(SAMPLE_STATIONS[2])
    False
    >>> has_kiosk(FAKE_STATIONS[2])
    False

    """
    return NO_KIOSK_LABEL not in station[1]


def get_station_info(station_id: int, stations: List['Station']) -> list:
    """Return a list containing the following information from stations
    about the station with id number station_id:
        - station name (str)
        - number of bikes available (int)
        - number of docks available (int)
        - whether or not the station has a kiosk (bool)
    (in this order)
    If station_id is not in stations, return an empty list.

    Precondition: stations has at most one station with id station_id.

    >>> get_station_info(7090, SAMPLE_STATIONS)
    ['Danforth Ave / Lamb Ave', 4, 10, True]
    >>> get_station_info(7571, SAMPLE_STATIONS)
    ['Highfield Rd / Gerrard St E - SMART', 14, 5, False]
    >>> get_station_info(1001, FAKE_STATIONS)
    ['Street Ave / Road Ave', 20, 0, True]
    >>> get_station_info(104, MY_STATIONS)
    ['station 104 - SMART', 22, 7, False]

    """
    index = 0
    while stations[index][ID] != station_id:
        index = index + 1
    new_list = [stations[index][NAME], stations[index][BIKES_AVAILABLE],
                stations[index][DOCKS_AVAILABLE], has_kiosk(stations[index])]
    return new_list


def get_total(index: int, stations: List['Station']) -> int:
    """Return the sum of the column in stations given by index. Return 0
    if stations is empty.

    Preconditions: index is a valid index into each station in stations.
                   The items in stations at the position that index
                    refers to are ints.

    >>> get_total(BIKES_AVAILABLE, SAMPLE_STATIONS)
    23
    >>> get_total(DOCKS_AVAILABLE, SAMPLE_STATIONS)
    32
    >>> get_total(BIKES_AVAILABLE, MY_STATIONS)
    26

    """
    total = 0
    for item in stations:
        total += item[index]
    return total


def get_station_with_max_bikes(stations: List['Station']) -> list:
    """Return the station id of the station that has the most bikes
    available.  If there is a tie for the most available, return the
    station id that appears first in stations.

    Preconditions: len(stations) > 0

    >>> get_station_with_max_bikes(SAMPLE_STATIONS)
    7571
    >>> get_station_with_max_bikes(HANDOUT_STATIONS)
    7000
    >>> get_station_with_max_bikes(FAKE_STATIONS)
    1001

    """
    station_id = stations[0][ID]
    max_bikes = stations[0][BIKES_AVAILABLE]
    for station in stations:
        if station[BIKES_AVAILABLE] > max_bikes:
            max_bikes = station[BIKES_AVAILABLE]
            station_id = station[ID]
    return station_id


def get_stations_with_n_docks(num: int, stations: List['Station']) -> List[int]:
    """Return a list containing the station ids for the stations in
    stations that have at least num docks available, in the same order
    as they appear in stations.

    Precondition: num >= 0

    >>> get_stations_with_n_docks(2, SAMPLE_STATIONS)
    [7090, 7486, 7571]
    >>> get_stations_with_n_docks(12, SAMPLE_STATIONS)
    [7486]
    >>> get_stations_with_n_docks(10, FAKE_STATIONS)
    [1000, 1003]
    >>> get_stations_with_n_docks(9, MY_STATIONS)
    [101, 103]

    """
    stations_with_n_docks = []
    i = 0
    while i < len(stations):
        if stations[i][DOCKS_AVAILABLE] >= num:
            stations_with_n_docks.append(stations[i][ID])
        i = i + 1
    return stations_with_n_docks


def get_direction(start_id: int, end_id: int, stations: List['Station']) -> str:
    """Return the direction to travel to get from station start_id to
    station end_id according to data in stations. Possible directions
    are defined by DIRECTIONS.

    Preconditions: start_id and end_id appears in stations.
                   start_id and end_id are ids of stations at different
                   locations.

    >>> get_direction(7486, 7090, SAMPLE_STATIONS)
    'SOUTHWEST'
    >>> get_direction(1000, 1002, FAKE_STATIONS)
    'NORTH'
    >>> get_direction(7000, 7001, HANDOUT_STATIONS)
    'NORTHEAST'
    >>> get_direction(7571, 7486, SAMPLE_STATIONS)
    'NORTHEAST'
    >>> get_direction(100, 104, MY_STATIONS)
    'SOUTH'
    >>> get_direction(101, 103, MY_STATIONS)
    'EAST'
    """
    #a list which contains the x and y components of the starting point
    #longitude: x-component, latitude: y-component
    start_point = get_long_and_lat(start_id, stations)
    #a list which contains the x and y components of the end point
    end_point = get_long_and_lat(end_id, stations)
    direction = ""
    if end_point[1] > start_point[1]:
        direction += NORTH
    elif end_point[1] < start_point[1]:
        direction += SOUTH
    if end_point[0] > start_point[0]:
        direction += EAST
    elif end_point[0] < start_point[0]:
        direction += WEST
    return direction


def get_nearest_station(lat: float, lon: float, with_kiosk: bool,
                        stations: List['Station']) -> int:
    """Return the id of the station from stations that is nearest to the
    location given by lat and lon.  If with_kiosk is True, return the
    id of the closest station with a kiosk.

    In the case of a tie, return the ID of the first station in
    stations with that distance.

    Preconditions: len(stations) > 1

    If with_kiosk, then there is at least one station in stations with a kiosk.

    >>> get_nearest_station(43.671134, -79.325164, False, SAMPLE_STATIONS)
    7571
    >>> get_nearest_station(43.674312, -79.299221, True, SAMPLE_STATIONS)
    7486
    >>> get_nearest_station(44, -80, False, MY_STATIONS)
    101
    >>> get_nearest_station(41, -70, False, FAKE_STATIONS)
    1003

    """
    station_id = stations[0][ID]
    nearest_distance = get_distance(lat, lon, stations[ID][LATITUDE],
                                    stations[ID][LONGITUDE])
    for station in stations:
        if with_kiosk and has_kiosk(station):
            distance = abs(get_distance(lat, lon, station[LATITUDE],
                                        station[LONGITUDE]))
            if distance < nearest_distance:
                nearest_distance = distance
                station_id = station[ID]
        else:
            distance = abs(get_distance(lat, lon, station[LATITUDE],
                                        station[LONGITUDE]))
            if distance < nearest_distance:
                nearest_distance = distance
                station_id = station[ID]
    return station_id


def rent_bike(station_id: int, stations: List['Station']) -> bool:
    """Update the available bike count and the docks available count for
    the station in stations with id station_id as if a single bike was
    removed, leaving an additional dock available. Return True if and
    only if the rental was successful, i.e. there was at least one
    bike available and the station is renting.

    Precondition: station_id appears in stations.

    >>> stations = copy.deepcopy(SAMPLE_STATIONS)
    >>> rent_bike(7090, stations)
    True
    >>> stations[0][BIKES_AVAILABLE]
    3
    >>> stations[0][DOCKS_AVAILABLE]
    11
    >>> rent_bike(7486, stations)
    False
    >>> stations[1][BIKES_AVAILABLE]
    5
    >>> stations[1][DOCKS_AVAILABLE]
    17
    >>> rent_bike(104, MY_STATIONS)
    False
    >>> rent_bike(1001, FAKE_STATIONS)
    True

    """
    for station in stations:
        if station[ID] == station_id:
            if station[IS_RENTING] is True and station[BIKES_AVAILABLE] > 0:
                station[BIKES_AVAILABLE] = station[BIKES_AVAILABLE] - 1
                station[DOCKS_AVAILABLE] = station[DOCKS_AVAILABLE] + 1
                return True
    return False


def return_bike(station_id: int, stations: List['Station']) -> bool:
    """Update the available bike count and the docks available count for
    station in stations with id station_id as if a single bike was
    added, making an additional dock unavailable. Return True if and
    only if the return was successful, i.e. there was at least one
    dock available and the station is allowing returns.

    Precondition: station_id appears in stations.

    >>> stations = copy.deepcopy(SAMPLE_STATIONS)
    >>> return_bike(7090, stations)
    True
    >>> stations[0][BIKES_AVAILABLE]
    5
    >>> stations[0][DOCKS_AVAILABLE]
    9
    >>> return_bike(7486, stations)
    False
    >>> stations[1][BIKES_AVAILABLE]
    5
    >>> stations[1][DOCKS_AVAILABLE]
    17
    >>> return_bike(100, MY_STATIONS)
    True
    >>> return_bike(7486, SAMPLE_STATIONS)
    False

    """
    for item in stations:
        if item[ID] == station_id:
            if item[DOCKS_AVAILABLE] > 0 and item[IS_RETURNING]:
                item[BIKES_AVAILABLE] = item[BIKES_AVAILABLE] + 1
                item[DOCKS_AVAILABLE] = item[DOCKS_AVAILABLE] - 1
                return True
    return False


def balance_all_bikes(stations: List['Station']) -> int:
    """Return the difference between the number of bikes rented and the
    number of bikes returned as a result of the following balancing:

    Calculate the percentage of bikes available across all stations
    and evenly distribute the bikes so that each station has as close
    to the overall percentage of bikes available as possible. Remove a
    bike from a station if and only if the station is renting and
    there is a bike available to rent, and return a bike if and only
    if the station is allowing returns and there is a dock available.

    >>> stations = copy.deepcopy(SAMPLE_STATIONS)
    >>> balance_all_bikes(stations)
    4
    >>> stations == [
    ...  [7090, 'Danforth Ave / Lamb Ave',
    ...   43.681991, -79.329455, 15, 6, 8, True, True],    # return 2
    ...  [7486, 'Gerrard St E / Ted Reeve Dr',
    ...   43.684261, -79.299332, 22, 5, 17, False, False], # no change
    ...  [7571, 'Highfield Rd / Gerrard St E - SMART',
    ...   43.671685, -79.325176, 19, 8, 11, True, True]]   # rent 6
    True
    >>> stations = copy.deepcopy(HANDOUT_STATIONS)
    >>> balance_all_bikes(stations)
    0
    >>> stations == [
    ...  [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 17,
    ...   14, True, True],
    ...  [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,
    ...   15, 8, 7, True, True]]
    True

    """
    return_bikes = 0
    rent_bikes = 0
    percentage = calculate_target_percentage(stations)

    for station in stations:
        num_of_bikes = round(station[CAPACITY] * percentage)
        if num_of_bikes > station[BIKES_AVAILABLE] and station[IS_RETURNING]:
            if station[DOCKS_AVAILABLE] >= (num_of_bikes -
                                            station[BIKES_AVAILABLE]):
                return_bikes += num_of_bikes - station[BIKES_AVAILABLE]
                station[DOCKS_AVAILABLE] -= (num_of_bikes -
                                             station[BIKES_AVAILABLE])
                station[BIKES_AVAILABLE] = num_of_bikes
            else:
                return_bikes += station[DOCKS_AVAILABLE]
                station[BIKES_AVAILABLE] += station[DOCKS_AVAILABLE]
                station[DOCKS_AVAILABLE] = 0
        elif num_of_bikes < station[BIKES_AVAILABLE] and station[IS_RENTING]:
            rent_bikes += station[BIKES_AVAILABLE] - num_of_bikes
            station[DOCKS_AVAILABLE] += station[BIKES_AVAILABLE] - num_of_bikes
            station[BIKES_AVAILABLE] = num_of_bikes
    return rent_bikes - return_bikes

# We suggest using this as a helper function for the function
# balance_all_bikes.
def calculate_target_percentage(stations: List['Station']) -> float:
    """Return the target percentage of available bikes at each station
    from stations, for the purpose of re-balancing.

    >>> target_percent = calculate_target_percentage(FAKE_STATIONS)
    >>> abs(target_percent - 0.625) < EPSILON
    True
    >>> calculate_target_percentage(MY_STATIONS)
    0.5
    >>> target_percent = calculate_target_percentage(SAMPLE_STATIONS)
    >>> abs(target_percent - 0.625) < EPSILON
    False

    """
    target_percentage = get_total(5, stations) / get_total(4, stations)
    return target_percentage


def get_station(station_id: int, stations: List['Station']) -> 'Station':
    """Return the stations from stations with id station_id. If there is
    no such station, return the empty list.

    >>> station = [7486, 'Gerrard St E / Ted Reeve Dr', 43.684261, -79.299332,
    ...            22, 5, 17, False, False]
    >>> get_station(7486, SAMPLE_STATIONS) == station
    True
    >>> get_station(100, MY_STATIONS)
    [100, 'station 100', -40, 80, 12, 1, 2, True, True]

    """
    new_list = []
    for element in stations:
        if element[ID] == station_id:
            new_list = element
    return new_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # To test your code with larger lists, you can uncomment the code
    # below to read data from the provided CSV file.
    stations_file = open('stations.csv')
    bike_stations = csv_to_list(stations_file)
    clean_data(bike_stations)

    # For example,
    # print('Testing get_station_with_max_bikes: ',
    #    get_station_with_max_bikes(bike_stations) == 7037)
    