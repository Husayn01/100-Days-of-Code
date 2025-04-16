import requests
import config
from twilio.rest import Client

url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = config.api_key
account_sid = config.account_sid
auth_token = config.auth_token

weather_params = {
    "lat": 9.0570752,
    "lon": 7.4481664,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url, params=weather_params)
data = response.json()

will_rain = False

for hour_data in data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code > 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
    content_variables='{"1":"12/1","2":"3pm"}',
    to='whatsapp:+2349031852400'
    )
    print(message.sid)


