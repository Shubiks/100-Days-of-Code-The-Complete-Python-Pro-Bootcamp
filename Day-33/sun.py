import requests
import datetime
import smtplib
import time

MY_LAT = 11.341036
MY_LNG = 77.717163

email = "s35351342@gmail.com"
password = "vbzlgbwkiuyaxgps"

parameters = {
    "lat": MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

def is_above_me():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()

    long = float(data["iss_position"]['longitude'])
    lat = float(data["iss_position"]['latitude'])

    return MY_LAT-5<=long<= MY_LAT+5 and MY_LNG-5<=lat<=MY_LNG+5



def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = datetime.datetime.now().hour
    if now >=sunset or now<= sunrise:
        return True

while True:
    time.sleep(60)

    if is_above_me() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
        )
        connection.close()