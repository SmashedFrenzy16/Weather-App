import requests as rq
from time import strftime, gmtime
from suntime import Sun, SunTimeException
from sys import exit

api = input("Enter in your API key: ")

def main():

    city = input("Enter in the city name: ")

    units = input("Enter in the units you want (metric/imperial): ")


    try:


        final_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api}"

        weather_data = rq.get(final_url).json()

        lat = weather_data["coord"]["lat"]
        long = weather_data["coord"]["lon"]

        coords = Sun(lat, long)

        sunrise_time = coords.get_sunrise_time()
        sunset_time = coords.get_sunset_time()

        weather_type = weather_data["weather"][0]["main"]
        weather_des = weather_data["weather"][0]["description"]

        current_temp = weather_data["main"]["temp"]
        feels_like_temp = weather_data["main"]["feels_like"]
        min_temp = weather_data["main"]["temp_min"]
        max_temp = weather_data["main"]["temp_max"]

        pressure = weather_data["main"]["pressure"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        wind_deg = weather_data["wind"]["deg"]

        if units == "metric":

            print("\n\nLocation Weather Details:")
            print(f"City: {city}")
            print(f"\nWeather: {weather_type}, {weather_des}")
            print(f"Current Temperature: {current_temp}°C (Feels Like: {feels_like_temp}°C)")
            print(f"Minimum Temperature Today: {min_temp}°C")
            print(f"Maximum Temperature Today: {max_temp}°C")
            print(f"\nPressure: {pressure}")
            print(f"Humidity: {humidity}")
            print(f"Wind Details: Speed: {wind_speed} Direction: {wind_deg}°")
            print(f"\nSunrise: {sunrise_time}")
            print(f"Sunset: {sunset_time}")

        elif units == "imperial":

            print("\n\nLocation Weather Details:")
            print(f"City: {city}")
            print(f"\nWeather: {weather_type}, {weather_des}")
            print(f"Current Temperature: {current_temp}°F (Feels Like: {feels_like_temp}°F)")
            print(f"Minimum Temperature Today: {min_temp}°F")
            print(f"Maximum Temperature Today: {max_temp}°F")
            print(f"\nPressure: {pressure}")
            print(f"Humidity: {humidity}")
            print(f"Wind Details: Speed: {wind_speed} Direction: {wind_deg}°")
            print(f"\nSunrise: {sunrise_time}")
            print(f"Sunset: {sunset_time}")

    except SunTimeException as e:

        print(e)

    except:

        print("Error while fetching data. Please check that your details are correct and check your internet connection.")

while True:

    main()

    repeat = input("Would you like to display the weather details for another city (y/n)?: ")

    if repeat == "Y" or repeat == "y":

        main()

    else:

        exit()
