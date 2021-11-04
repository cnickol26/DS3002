# -*- coding: utf-8 -*-

# -- Sheet --

import json
import requests
import csv
import time

#1 Grab a list of quotes to get form Yahoo
# Replace ORCL with desired stock ticker
querystring = {"symbols":"APPL"}

apikey='zUC1HxQqE953P43MM9mXZ9Y0LjK77zkw7qPfPBC0'


url = "https://yfapi.net/v6/finance/quote"
headers = {
  'x-api-key': apikey
   }

response = requests.request("GET", url, headers=headers, params=querystring)
#print(response.text)
response.raise_for_status()  # raises exception when not a 2xx response
#if response.status_code != 204:

timestamp=int(time.time())
stock_time = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(timestamp))
print(stock_time)
stock_json = response.json()
data=[stock_json['quoteResponse']['result'][0]["displayName"], stock_time ,str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"])]

#Stock prices is my CSV I created
with open("Stock Prices", "w") as f:
    writer = csv.writer(f)
    writer.writerow(data)

#I attempted to implement a function that would take the ticker as the input but ran into errors I couldn't solve. I also tried to write some if statements to deal with potential erroneous tickers but was unable to accomplish this. I also could not get the stock_time to save in my data row, this must just be a formatting issue I was unable to figure out

