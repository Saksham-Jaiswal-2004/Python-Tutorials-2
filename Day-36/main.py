import requests
from pyexpat.errors import messages
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = (difference/float(yesterday_closing_price))*100
print(diff_percent)

# If TODO4 percentage is greater than 5 then print("Get News").

if diff_percent > 4:
    print("Get News")

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if diff_percent > 4:
    news_params = {
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME
    }
    news_data = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_data.json()["articles"]

# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formatted_articles_list = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio.

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles_list:
    message = client.messages.create(
        body=article,
        from_="",
        to = ""
    )