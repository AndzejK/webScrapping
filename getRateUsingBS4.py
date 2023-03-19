from bs4 import BeautifulSoup
import requests

def get_currency_rate(in_cur, out_cur):
    url = f"https://www.x-rates.com/calculator/?from={in_cur}&to={out_cur}&amount=1"
    # if you enter "EUR","AUD" the result would be https://www.x-rates.com/calculator/?from=EUR&to=AUD&amount=1
    get_content=requests.get(url).text # getting SOURCE CODE 

    # At this stage we start using bs4 lib
    soup = BeautifulSoup(get_content,"html.parser")
    # finding class for our rate in HTML format
    soup.find("span", class_="ccOutputRslt")
    # display just text as browser for an user!
    rate=soup.find("span", class_="ccOutputRslt").get_text() # result is 1.598466 AUD and we want to have just numbers
    rate=float(rate[:-4])
    return rate

today_rate_is=get_currency_rate("EUR","AUD")
print(today_rate_is)