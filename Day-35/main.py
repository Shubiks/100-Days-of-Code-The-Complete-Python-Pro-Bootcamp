import requests
from twilio.rest import Client

parameters ={
    "lat": 40.993599,
    "lon": 71.677452,
    "appid": "467cbb0f575591d5afc96b915836d8df",
    "cnt":4
}


response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()  # Check for request errors
data = response.json()

data_list = data["list"]
data_dict={}
id = []

for d in data_list:
    data_dict[d["dt_txt"]] = {
        "weather_id": d["weather"][0]["id"],
        "description": d["weather"][0]["description"]
    }
    id.append(d["weather"][0]["id"])

for i in id:
    if i <700:
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="It's going to rain take an ☔.",
            from_="",
            to="",
        )

        print(message.Status)
        break
    