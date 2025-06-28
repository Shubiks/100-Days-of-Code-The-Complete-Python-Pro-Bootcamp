import requests
import datetime

TOKEN = "hjyfdsfub689sdfbid9fds3bdjfgi"
NAME = "shubi"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params={
    "token": TOKEN,
    "username":NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_end_point = f"{pixela_endpoint}/{NAME}/graphs"

header = {
    "X-USER-TOKEN" :TOKEN
}

graph_params = {
    "id": "graph1",
    "name":"CycleTracker",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_end_point,json=graph_params,headers=header)
# print(response.text)

track_endpoint = f"{pixela_endpoint}/{NAME}/graphs/{GRAPH_ID}"

today = datetime.datetime(year=2025,month=6,day=13)


track_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.8"
}

# response = requests.post(url=track_endpoint,headers=header,json=track_body)
# print(response.text)

formatted_date = today.strftime("%Y%m%d")

update_track_endpoint = f"{track_endpoint}/{formatted_date}"

update_body = {
    "quantity": "9.5"
}

# response = requests.put(url=update_track_endpoint,headers=header,json=update_body)
# print(response.text)

delete_endpoint = f"{update_track_endpoint}"

response = requests.delete(url=delete_endpoint,headers=header)
