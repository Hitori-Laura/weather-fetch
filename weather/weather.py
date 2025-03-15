import geocoder
import requests
from colorama import Fore, Back, Style
import os

def main():
    # Get current location based on IP address
    g = geocoder.ip('me')
    
    script_dir = os.path.dirname(__file__)
    ascii_art_path = os.path.join(script_dir, 'ASCII_art')
    printcity = str.capitalize(input('Do you want to show the city name? "Y, N": '))

    if printcity == "Y":
        print(Fore.GREEN + "City detected: " + g.city)
    elif printcity == "N":
        print(Fore.GREEN + "City successfully detected")
    
    # Define the city as a variable
    city = g.city

    # Coordinates for the city
    latitude = g.lat
    longitude = g.lng

    # Construct the API request URL using the coordinates
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    # Make the API request
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()
    weather_code = data['current_weather']['weathercode']

    # Print the weather information
    if printcity == "Y":
        print(Fore.RED + f"Weather in {city}:")
    else:
        print(Fore.RED + "The weather:")
    
    # Define weather conditions
    if weather_code == 0:
        with open(os.path.join(ascii_art_path, "sunny.txt"), "r") as file:
            print(Fore.YELLOW + file.read())
        print("It's sunny")
    elif weather_code in [1, 2, 3]:  # Partly cloudy to overcast (could still be sunny)
        with open(os.path.join(ascii_art_path, "cloudy.txt"), "r") as file:
            print(Fore.YELLOW + file.read())
        print("It's partly cloudy")
    elif weather_code in [45, 48]:  # Fog
        with open(os.path.join(ascii_art_path, "foggy.txt"), "r") as file:
            print(Fore.BLUE + file.read())
        print("It's foggy")
    elif weather_code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:  # Rain codes
        with open(os.path.join(ascii_art_path, "/rainy.txt"), "r") as file:
            print(Fore.BLUE + file.read())
        print("It's raining")
    else:
        print("Weather condition unknown")

    print(Fore.RED + f"Temperature: {data['current_weather']['temperature']}°C")
    print(Fore.YELLOW + f"Wind Speed: {data['current_weather']['windspeed']} km/h")
    print(Fore.BLUE + f"Wind Direction: {data['current_weather']['winddirection']}°")
    print(Style.RESET_ALL)
