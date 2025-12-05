# Google has now blocked weather scraping.
# So it’s no longer possible to fetch weather from Google using BeautifulSoup.
"""
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'
}

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}',
        headers=headers
    )
    print("Searching .......... \n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    temperature = soup.select('#wob_tm')[0].getText().strip()

    print(location)
    print(time)
    print(info)
    print(temperature + "°C")

city = input("Enter the Name of Any city >> ")
city = city + " weather"
weather(city)
"""

# Now replace this program using wttr.in API — no key required, always works.
import requests

def weather(city):
    # Step 1: Convert city to latitude & longitude
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_data = requests.get(geo_url).json()

    if "results" not in geo_data:
        print("❌ City not found!")
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    # Step 2: Fetch current weather
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    data = requests.get(weather_url).json()

    temp = data["current_weather"]["temperature"]
    wind = data["current_weather"]["windspeed"]

    print(f"\nWeather in {city.capitalize()}:")
    print("Temperature:", temp, "°C")
    print("Wind Speed:", wind, "km/h")

city = input("Enter the Name of Any City >> ")
weather(city)


"""
Enter the Name of Any City >> Mumbai
Weather in Mumbai:
Temperature: 27.5 °C
Wind Speed: 14.9 km/h

Enter the Name of Any City >> Delhi
Weather in Delhi:
Temperature: 13.6 °C
Wind Speed: 4.4 km/h

"""

