import requests
import util
from datetime import datetime, timedelta, timezone
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PRICE_UP = "🔺"
PRICE_DOWN = "🔻"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yesterday's closing stock price.
today = datetime.now(timezone.utc).date()


def get_stock_price_diff():
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": config["stock_api_key"]
    }
    r = requests.get(STOCK_ENDPOINT, params=params)
    data = r.json()["Time Series (Daily)"]

    # {'1. open': '343.5000', '2. high': '348.0200', '3. low': '333.3300', '4. close': '342.6900', '5. volume': '81873829'}
    data_list = [value for (key, value) in data.items()]
    yesterday_close = float(data_list[0]["4. close"])
    day_b4_yesterday_close = float(data_list[1]["4. close"])

    price_diff = yesterday_close - day_b4_yesterday_close
    price_change = round((abs(price_diff) / day_b4_yesterday_close) * 100, 0)

    return  {
        "price_difference": price_diff,
        "price_percent_change": price_change
    }


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
# GET https://newsapi.org/v2/everything?q=Apple&from=2025-06-04&sortBy=popularity&apiKey=API_KEY
def get_stock_news():
    params = {
        "qInTitle": COMPANY_NAME,
        "from": today,
        "sortBy": "popularity",
        "apiKey": config["news_api_key"]
    }

    r = requests.get(NEWS_ENDPOINT, params=params)
    data = r.json()["articles"][:3]
    return data # 1st 3 new articles
    # data["articles"][n]["title"], data["articles"][n]["description"]


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
def send_whatsapp(messages):

    client = Client(config["account_sid"], config["3b67da36ba9f57f4c6177f835e628d96"])
    for msg in messages:
        message = client.messages.create(
            from_=f'whatsapp:{config["whatsapp_from"]}',
            body=msg,
            to=f'whatsapp:{config["whatsapp_to"]}'
        )
        print(message.status)


config = util.read_config()
stock_change = get_stock_price_diff()
if stock_change["price_percent_change"] > 5:
    print("stock change > 5% ")
    if stock_change["price_difference"] < 0:
        stock_move = f"{PRICE_DOWN} {stock_change["price_percent_change"]}%"
    else:
        stock_move = f"{PRICE_UP} {stock_change["price_percent_change"]}%"

    stock_news = get_stock_news()
    email_msgs = [f"Subject:{STOCK}: {stock_change}\n\nHeadline: {news['title']}\nBrief: {news['description']}" for news in
                  stock_news]
    util.email_me_messages(email_msgs, config)

    # sms_msgs = [f"{STOCK}: {stock_change} - {news['title']}" for news in stock_news]
    # send_whatsapp(sms_msgs)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

