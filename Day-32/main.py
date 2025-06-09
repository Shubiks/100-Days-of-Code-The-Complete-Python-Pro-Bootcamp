import smtplib

email = "s35351342@gmail.com"
password ="vbzlgbwkiuyaxgps"


## what ever the connection to be closed can use with
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    # subject = "Test Email"
    # body = "Hello, this is a test email."
    # msg = f"Subject: {subject}\n\n{body}"
    connection.sendmail(from_addr=email,to_addrs=email,msg="Hello")