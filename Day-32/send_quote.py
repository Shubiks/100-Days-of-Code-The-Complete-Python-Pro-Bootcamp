import smtplib
import random
import datetime as dt

email = "s35351342@gmail.com"
password = "vbzlgbwkiuyaxgps"

with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)


# with open(smtplib.SMTP("smtp.gmail.com",587)) as connection:
tdy = dt.datetime.now()
if tdy.weekday()==0:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs=email,msg=quote)