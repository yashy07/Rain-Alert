import requests
import os
from twilio.rest import Client
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
parameters = {
    'lat':19.141406
    ,'lon':72.957184,
    "appid": api_key,
    "cnt":4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
weather_data = response.json()
will_rain=False
Condition_list =[weather_data['list'][x]['weather'][0]['id'] for x in range(0,len(weather_data['list']))]
for condition_code in Condition_list:
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages .create(
        body="It's going to rain today! Remember to bring an ☂️ ",
        from_="+17244425941",
        to="+917977053601"
    )
    print("Bring an umbrella!")
