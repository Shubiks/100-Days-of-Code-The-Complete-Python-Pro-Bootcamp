import requests
import datetime

API_KEY = "0abfeb6332e457746a2cd21d8b1b9ad6"
APP_ID = "de57464d"
Nutritionix_url = "https://trackapi.nutritionix.com"

user_input = str(input("What did you do today? "))

header = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

parse_url = f"{Nutritionix_url}/v2/natural/nutrients"
exercise_url = f"{Nutritionix_url}/v2/natural/exercise"

parse_body = {
    "query":user_input
}

today = datetime.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
exercise_data = {
    "workout":{

    }
}

response = requests.post(url=exercise_url,headers=header,json=parse_body)

data = response.json()
exercises = data["exercises"]

sheet_url = "https://api.sheety.co/b115710bb695c3ac64867792bf257263/myWorkoutsProject/workouts"
sheet_header = {
    "Authorization": "Bearer SDFG345bjdhbhHIG898u9hbHGHIjwoejL"
}

for d in range(len(exercises)):
    exercise_data["workout"]["date"] = date
    exercise_data["workout"]["time"] = time
    exercise_data["workout"]["exercise"] = exercises[d]["name"]
    exercise_data["workout"]["duration"] = exercises[d]["duration_min"]
    exercise_data["workout"]["calories"] = exercises[d]["nf_calories"]

    response = requests.post(url=sheet_url,json=exercise_data,headers=sheet_header)
    print(response.json())
    

    
