import requests
from twilio.rest import Client

API_KEY = '<api_key>'
ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
ACCOUNT_SID = '<sid>'
AUTH_TOKEN = '<token>'

# dictionary - must follow the keys provided in API docs
weather_params = {
    "lat": 123,
    "lon": 123,
    "appid": API_KEY,
    "cnt": 4,
}

# want to make our GET requests to the endpoint - check the data they already have, get it
# provide params = want type of data we get back (in this case its weather info)
response = requests.get(ENDPOINT, params=weather_params)

weather_data = response.json()
# print(weather_data['list'][0]['main']['feels_like'])

will_rain = False

for data in weather_data['list']:
    temp_k = data['main']['feels_like']
    temp_f = ((temp_k - 273.15) * 1.8) + 32
    formatted_temp_f = '%.1f' % temp_f
    print(formatted_temp_f)

for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) != 700:
        will_rain = True
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body='Its gonna rain today. Bring an umbrella',
            from_='sender',
            to='your number',
    )
    print(message.status)


