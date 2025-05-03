import os
import pandas as pd
import smtplib
import random
import datetime as dt
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()


Product_URL = "THE_PRODUCT_YOU_WANT_TO_TRACK"

headers = {
    "User-Agent": (
          "YOUR_USER_AGENT",
    ),
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=Product_URL, headers=headers)
Product_Web_Page = response.text

soup = BeautifulSoup(Product_Web_Page, "html.parser")
Price = soup.find(class_="a-offscreen")
txt = Price.getText().strip()
temp_price = txt.split("$")
final_price = temp_price[1]


# ------- SMTP ------- 


my_email = os.environ["MY_EMAIL"]
password = os.environ["MY_PASSWORD"]

target_price = input("What your tagert price for that product?: ")
conntents = f"The Price on the speakers you were looking for just dropped under {target_price}$!\n URL: {Product_URL} "


if float(final_price) < float(target_price):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Price Dropped!\n\n{conntents}"
        )
