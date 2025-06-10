import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
data = response.json()

long = data["iss_position"]['longitude']
lat = data["iss_position"]['latitude']

iss_position = (long,lat)
print(iss_position)