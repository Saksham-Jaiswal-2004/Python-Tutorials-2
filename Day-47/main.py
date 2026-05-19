import os
import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0",
    "accept-language": "en-US,en;q=0.9"
}

response = requests.get(os.environ["SITE_URL"], headers=headers)
web_data = response.text

soup = BeautifulSoup(web_data, "html.parser")

price = soup.find("span", class_="a-offscreen").get_text()
print(price)
final_price = float(price.split("INR")[1].replace(",", ""))
print(final_price)

title = soup.find(id="productTitle").getText().strip()
print(title)

BUY_PRICE = 14000

if final_price <= BUY_PRICE:
    message = f"{title} is on sale for {final_price}!"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(from_addr=os.environ["EMAIL_ADDRESS"], to_addrs=os.environ["EMAIL_ADDRESS"], msg=f"Subject:Amazon Price Alert!\n\n{message}\n{os.environ['SITE_URL']}".encode("utf-8"))
        print("Email Sent Successfully!")