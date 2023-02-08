import requests
import geopy.geocoders

#######################------------------------you can add the api key hear , without api key you cannot access this-------------------###########

API_KEY = "your_api_key_here"
GEOLOCATOR = geopy.geocoders.Nominatim(user_agent="geoapiExercises")

def get_location():
    location = GEOLOCATOR.geocode(None, exactly_one=False)
    return location[0].latitude, location[0].longitude

def get_temperature(api_key, latitude, longitude):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()s
        temperature = data["main"]["temp"] - 273.15
        return temperature
    else:
        return "Error: Could not retrieve temperature data."

latitude, longitude = get_location()
temperature = get_temperature(API_KEY, latitude, longitude)
print("The temperature at your location is {:.2f}°C".format(temperature))
