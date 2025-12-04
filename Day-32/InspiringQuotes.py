import random
import smtplib as sm
import datetime as dt

my_email = "cse24083@iiitkalyani.ac.in"
password = ""

connection = sm.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

now = dt.datetime.now()
day = now.weekday()

if day==3:
    with open("quotes.txt", "r") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)
    connection.sendmail(from_addr=my_email, to_addrs="sakshamgamer2004@gmail.com", msg=f"Subject:Today's Inspiration\n\n{quote}")

connection.close()