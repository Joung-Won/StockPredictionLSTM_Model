from grpc import composite_channel_credentials
import pandas_datareader  as pdr
import pandas as pd
import yfinance as yf
import datetime
from datetime import date
import time
import requests
import io
import numpy
import matplotlib.pyplot as plt


start = datetime.datetime(2010,1,1)
end = date.today()

url="https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv"

s = requests.get(url).content

companies = pd.read_csv(io.StringIO(s.decode('utf-8')))

symbols = ['nvda', 'fb', 'aapl', 'amzn', 'msft']
for s in symbols:
    df = pdr.DataReader(s, 'yahoo', start, end)
    df.to_csv(s + '.csv')


