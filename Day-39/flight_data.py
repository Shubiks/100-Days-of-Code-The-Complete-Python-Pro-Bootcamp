import requests
API_Key = "QcHna0LD1WL3GIALclGy6sYLrGAfpUkT"
API_Secret = "d7AgnlqVlHRXNkOQ"
ACCESS_TOKEN = "8SXAf2ju9wLy0Q2bC4f5R7BXyL9A"

base_url = "https://test.api.amadeus.com/v1"

iata_url = f"{base_url}/reference-data/locations"

header = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}


class FlightData:
    def __init__(self):
        pass

        


# access_url = "https://test.api.amadeus.com/v1/security/oauth2/token"

# access_params = {
#     "grant_type": "client_credentials",
#     "client_id":API_Key,
#     "client_secret":API_Secret
# }

# response = requests.post(url=access_url,data=access_params)
# print(response.json())