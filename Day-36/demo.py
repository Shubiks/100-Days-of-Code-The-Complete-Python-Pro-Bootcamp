import datetime
import requests
from twilio.rest import Client
import time

parameters ={
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": "QYDWKVZZGEUSNN4G"
}

url ="https://www.alphavantage.co/query"

response = requests.get(url, params=parameters)
data = response.json()


now = datetime.datetime.now()

prev_day = now - datetime.timedelta(days=1)
day_before_prev = now - datetime.timedelta(days=2)

prev_date = prev_day.date()
day_before_prev_date = day_before_prev.date()

# print(prev_date, day_before_prev_date)
# print(data)

prev_day_data= data["Time Series (Daily)"][f"{prev_date}"]["4. close"]
day_before_prev_data = data["Time Series (Daily)"][f"{day_before_prev_date}"]["4. close"]

# print(prev_day_data)
# print(day_before_prev_data)

diff_closing_price = float(prev_day_data) - float(day_before_prev_data)

up_down = None
if diff_closing_price < 0:
    up_down = "🔻"
else:
    up_down = "🔺"

# print(diff_closing_price)

diff_percent = round((diff_closing_price / float(prev_day_data)) * 100)

# print(diff_percent)

news_param = {
    "q": "IBM",
    "apiKey": "14d2246a15ac478fa958c8d39bef4a40"
}
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

diff_percent = 1.33

if abs(diff_percent) > 1:
    newa_response = requests.get("https://newsapi.org/v2/everything", params=news_param)
    news_data = newa_response.json()
    top_articles = news_data["articles"][:3]
    
    # msg = [f"'Headline':{news['title']},'Brief':{news['description']}" for news in top_articles]
    msg = [f"{news_param['q']}: {up_down}{diff_percent}%\n'Headline':{news['title']},'Brief':{news['description']}" for news in top_articles]


    for m in msg:
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=m,
            from_="",
            to="",
        )

        print(message.Status)


 


 