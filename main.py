"""

Skill Challenge - Building A Cache

1. define a function 'get_weather(city)'
    that simulates the retrieval of weather data for a given city.

    For simplicity,
        the function will return a dictionary containing random values for temperature
        (range from -10 to 30) and humidity (range from 0 to 100).

        Use a delay of 1 second to mimic the real-time delay of calling a live API

2. then define a decorator 'cache_decorator(func)'
    that checks if the requested city's weather data is

    already in the cache AND it isn't too old (i.e. less than 10 seconds old).

    If the data meets both conditions, the decorator should return a value from cache rather
    than allow the invocation of the target function

    if the weather data for the city is not in the cache or it's too old,
    the 'get_weather(city)' invocation should be allowed to get and return fresh data.

In addition, the cache should be updated with the new data
    for simplicity, implement the weather data cache for each city as a dictionary

"""

import time
import random
from datetime import datetime


def cache_decorator(function):
    data = {}
    temperature = random.randint(-10, 30)
    humidity = random.randint(0, 30)
    current_time = time.ctime()[11:19]

    def time_compare(city, time_right_now):
        time_format = '%H:%M:%S'

        last_upd = data[city]['last_upd']

        last_upd_object = datetime.strptime(last_upd, time_format)
        current_time_object = datetime.strptime(time_right_now, time_format)

        time_difference = current_time_object - last_upd_object

        if time_difference.total_seconds() < 10:
            return True
        else:
            return False

    def wrapper(city):
        def returnal(local_data):
            sorted_data = list(local_data[city].values())  # [7, 29, '05:59:16']

            final_answer = f"""
The temperature in {city} is {sorted_data[0]}, and the humidity index is {sorted_data[1]}.            
"""
            return final_answer

        if city not in data:
            data[city] = {"temperature": temperature, "humidity": humidity, 'last_upd': current_time}
            return returnal(local_data=data)
        else:
            time_check = time_compare(city=city, time_right_now=current_time)

            if time_check:
                return returnal(local_data=data)
            else:
                data[city] = {"temperature": temperature, "humidity": humidity, 'last_upd': current_time}
                return returnal(local_data=data)

    return wrapper


@cache_decorator
def get_weather(city, result=None):
    time.sleep(1)
    return result


print(get_weather("Toronto"))
time.sleep(5)
print(get_weather("Toronto"))
print(get_weather("New York"))
