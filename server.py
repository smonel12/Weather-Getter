import requests
import datetime

key = '315ff1e75f172edd76f71aa5afccbc16'


def get_info(city_name, key):
    """
    Gets the weather and date-time information from the OpenWeather API.
    Returns it as a dictionary.
    """
    request_string = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'

    info = requests.get(request_string).json()

    dt = datetime.datetime.fromtimestamp(info['dt'])

    info['time'] = 'Time is ' + dt.strftime('%I:%M %p')

    info['date'] = 'Today is ' + dt.strftime('%b %d %Y')

    info['temperature'] = 'Temp is ' + str(kelvin_to_fahrenheit(info['main']['temp'])) + ' deg F'

    info['weather'] = 'Weather: {}'.format(info['weather'][0]['main'])

    info['humidity'] = 'Humidity is ' + str(info['main']['humidity']) + '%'

    info['pressure'] = 'Pressure is ' + str(info['main']['pressure']) + ' hPa'

    return info


def kelvin_to_fahrenheit(temp):
    """
    Given a temperature in kelvin, returns the corresponding
    temperature in fahrenheit.
    """
    return round((temp - 273.15) * 9 / 5 + 32)


def request(city, key):
    """
    Handles the request sent in by the ESP32. Returns an already formatted
    string for the ESP32 to print out.
    """
    information = get_info(city, key)
    all_info = []
    all_info.append(information['name'])
    all_info.append(information['date'])
    all_info.append(information['time'])
    all_info.append(information['temperature'])
    all_info.append(information['weather'])
    all_info.append(information['humidity'])
    all_info.append(information['pressure'])
    all_info = "\n".join(all_info)
    return all_info


city_name = input("What city do you want to know current weather for: ")
print(request(city_name, key))
