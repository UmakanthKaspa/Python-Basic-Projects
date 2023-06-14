import requests

API_KEY = 'd6a67eef89d65e78e0aff026bc2cec14'

def get_weather(api_key, location):
    url = f'http://api.weatherstack.com/current'
    params = {
        'access_key': api_key,
        'query': location
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'current' not in data:
        print(f"Error: Unable to fetch weather data for {location}")
        return

    current = data['current']
    print(f"Weather in {location}:")
    print(f"Temperature: {current.get('temperature')}°C")
    print(f"Weather Description: {', '.join(current.get('weather_descriptions', []))}")
    print(f"Wind Speed: {current.get('wind_speed')} km/h")
    print(f"Humidity: {current.get('humidity')}%")

def main():
    while True:
        location = input("Enter a location (or 'exit' to quit): ")
        
        if location.lower() == 'exit':
            break
        
        print("Fetching weather data...\n")
        get_weather(API_KEY, location)

if __name__ == '__main__':
    main()