import smtplib
import random
import datetime as dt
import pandas


data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
data = data.to_dict(orient="records")

def send_mail(email,name):
    to = email
    fro = email
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email,password="vbzlgbwkiuyaxgps")
        connection.sendmail(
            from_addr=fro,
            to_addrs=to,
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )
for d in range(len(data)):
    if data[d]["month"] == now.month and data[d]["day"] == now.day:
        send_mail(data[d]["email"], data[d]["name"])