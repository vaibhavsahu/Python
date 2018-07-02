#gets the latest price of this commodity from the web
import urllib2
import re
import time
from datetime import datetime
from sys import argv
from bs4 import BeautifulSoup
import json
import constants
import os
import csv
import arrow
from bs4 import BeautifulSoup, Comment
from decimal import Decimal


symbolName = ""


def get_last_price(url, commodity_code):
    headers = {'User-Agent': 'Mozilla'}
    try:
        req = urllib2.Request(url, None, headers)
        results = urllib2.urlopen(req).read()
        parsed = BeautifulSoup(results, 'html.parser')
        last_price_tag = parsed.find("span", id="last_last")
        symbolData = last_price_tag.contents
        data = symbolData[0].replace("'", '"')
        data = data.replace(",", "")
        data = float(str(data))
        return data
    except:
        return -1

while True:
    spx = get_last_price("https://www.investing.com/indices/us-spx-500-futures", 'spx') # S&P500
    gold = get_last_price("https://www.investing.com/commodities/gold", 'gold') # Gold
    oil = get_last_price("https://www.investing.com/commodities/crude-oil", 'oil') # Oil
    priceHistoryFile = constants.ROOTdata + "price" + ".txt"
    currentTimestamp = arrow.utcnow().to('US/Mountain').format('YYYY_MM_DD_HH_mm_ss')
    if not os.path.exists(os.path.dirname(priceHistoryFile)):
        os.makedirs(os.path.dirname(priceHistoryFile))
    with open(priceHistoryFile, 'a') as stream:
        writer = csv.writer(stream, delimiter='\t')
        writer.writerow((spx, oil, gold, currentTimestamp))






