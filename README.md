# Building A Cache

## Description

This Python code demonstrates the implementation of a cache using a decorator to store and retrieve weather data for different cities. The cache ensures that the weather data is up-to-date and reduces the need to make redundant API calls to fetch the same data within a short time interval.

---
## Task Description

1. Define a function `get_weather(city)` that simulates the retrieval of weather data for a given city. The function should return a dictionary containing random values for temperature (ranging from -10 to 30) and humidity (ranging from 0 to 100).

    - Use a delay of 1 second to mimic the real-time delay of calling a live API. This will make the function take some time to respond, similar to how a live API call might behave.

2. Implement a decorator `cache_decorator(func)` that checks if the requested city's weather data is already in the cache and if it's not older than 10 seconds. If the data meets both conditions, the decorator should return the value from the cache rather than allowing the invocation of the target function (`get_weather(city)`).

    - If the weather data for the city is not in the cache or it's too old (older than 10 seconds), the `get_weather(city)` invocation should be allowed to fetch and return fresh data.

3. The cache should be implemented for each city as a dictionary, where each city's weather data is stored along with the timestamp of the last update.

---
## Implementation Guidelines

- The `cache_decorator(func)` should be a separate function that takes a function `func` as an argument and returns a new function that implements the caching logic.

- The `get_weather(city)` function should return random temperature and humidity values for the given city.

- Use the `time.sleep(1)` function to introduce a 1-second delay in the `get_weather(city)` function to simulate the real-time delay of calling a live API.

- To compare timestamps, you can use the `datetime` module in Python.

## Example

```python
@cache_decorator
def get_weather(city):
    # Simulate API call delay
    time.sleep(1)

    # Simulate retrieving weather data
    temperature = random.randint(-10, 30)
    humidity = random.randint(0, 100)

    return {"temperature": temperature, "humidity": humidity}

print(get_weather("Toronto"))
time.sleep(5)
print(get_weather("Toronto"))
print(get_weather("New York")) 
```
---
## How the Code Works

1. The code defines a function `get_weather(city)` that simulates the retrieval of weather data for a given city. It returns a dictionary containing random values for temperature (ranging from -10 to 30) and humidity (ranging from 0 to 100).

2. The code defines a decorator `cache_decorator(func)` that checks if the requested city's weather data is already in the cache and if it's not older than 10 seconds. If the data meets both conditions, the decorator returns the value from the cache. Otherwise, it invokes the `get_weather(city)` function to fetch fresh data and updates the cache.

3. The cache is implemented as a dictionary called `data`, where each city's weather data is stored along with the timestamp of the last update.

4. The `time_compare(city, time_right_now)` function is used to compare the current time with the last update time of the city's weather data and determine if the data is up-to-date.

5. The `wrapper(city)` function inside the decorator handles the caching logic. It first checks if the city's data is already in the cache. If not, it fetches fresh weather data, adds it to the cache, and returns the formatted result. If the data is in the cache, it uses `time_compare` to check its freshness. If the data is fresh, it returns the cached result; otherwise, it fetches fresh data, updates the cache, and returns the result.

6. The `get_weather(city, result=None)` function is decorated with `cache_decorator`, allowing it to use caching when fetching weather data for a city. The function also includes a 1-second delay (`time.sleep(1)`) to mimic real-time delays in calling a live API.

7. The script calls `get_weather("Toronto")` twice, displaying the weather data for Toronto with caching applied for the second call.

8. The script then fetches and displays fresh weather data for the city of "New York."

---
