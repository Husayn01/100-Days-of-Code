
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# # print(response.status_code)
# # print(response)
# # print(response.json()['iss_position'])


# data = response.json()
# long = data['iss_position']["longitude"]
# lat = data['iss_position']["latitude"]

# iss_position = (long, lat)
# print(iss_position)

import requests
import datetime as dt

my_lat = 6.4444422
my_lng = 9.5436743
parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = dt.datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)
