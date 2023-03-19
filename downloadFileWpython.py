import requests
from datetime import datetime
import time

# Imitate a browser 
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#Trending ticker
ticker=input("Enter Trending ticker: ") # for Apple - AAPL; Micrsoft - MSFT

# Specify a date rage
from_date=input("Enter start date in yyyy/mm/dd format: ")
to_date=input("Enter end date in yyyy/mm/dd format: ")

#from and to _date we need to convert those strings into Epoch time
from_date=datetime.strptime(from_date,"%Y/%m/%d")
to_date=datetime.strptime(to_date,"%Y/%m/%d")

# get Epoch time and make sure that we don't have a float number!
from_epoch=int(time.mktime(from_date.timetuple()))
to_epoch=int(time.mktime(to_date.timetuple()))

link =f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"
give_me_content=requests.get(link,headers=headers).content

# make a file of this binary data
with open("Apple_stock_data.csv","wb") as csvFile:
    csvFile.write(give_me_content)

print(give_me_content)