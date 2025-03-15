import geocoder
import requests
import os
from colorama import Fore, Back, Style
def main():
     # Get current location based on IP address
     g = geocoder.ip('me')
     print(Fore.GREEN+"city detected: "+g.city)

     # Define the city as a variable
     city = g.city

     # Coordinates for the city
     latitude = g.lat
     longitude = g.lng

     #  Construct the API request URL using the coordinates
     url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

     # # Make the API request
     response = requests.get(url)
     
     

     # Parse the JSON response
     data = response.json()

     weather_code = data['current_weather']['weathercode']
     # # Print the weather information
     print(Fore.RED+f"Weather in {city}:")
     # Define weather conditions

     if weather_code == 0:
             file_path = os.path.join(os.path.dirname(__file__), 'ASCII_art', 'sunny.txt')
             with open(file_path, "r") as file:
                  print(Fore.YELLOW+file.read())
             print("It's sunny")
     elif weather_code in [1, 2, 3]: # Partly cloudy to overcast (could still be sunny)
             file_path = os.path.join(os.path.dirname(__file__), 'ASCII_art', 'cloudy.txt')
             with open(file_path, "r") as file:
                  print(Fore.YELLOW+file.read())
             print("It's partly cloudy")
     elif weather_code in [45, 48]:  # Fog
             file_path = os.path.join(os.path.dirname(__file__), 'ASCII_art', 'foggy.txt')
             with open(file_path, "r") as file:
                  print(Fore.BLUE+file.read())
             print("It's foggy")
     elif weather_code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:  # Rain codes
             file_path = os.path.join(os.path.dirname(__file__), 'ASCII_art', 'rainy.txt')
             with open(file_path, "r") as file:
                  print(Fore.BLUE+file.read())
             print("It's raining")
     else:
             print("Weather condition unknown")


     print(Fore.RED+f"Temperature: {data['current_weather']['temperature']}°C")
     print(Fore.YELLOW+f"Wind Speed: {data['current_weather']['windspeed']} km/h")
     print(Fore.BLUE+f"Wind Direction: {data['current_weather']['winddirection']}°")
     
