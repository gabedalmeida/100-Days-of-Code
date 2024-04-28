import requests
from twilio.rest import Client

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "244707c7060c04d06bf44ed42f5a0a70"



#50.110924
#8.682127

parameters = {
    
    "lat" : 57.70716,
    "lon" :  11.96679,
    "appid" : api_key,
    "cnt" : 4,
    
}


response = requests.get(OWN_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False




for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain= True
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella.☔️",
        from_='+12294711816',
        to='+491727086'
    )

    print(message.status)