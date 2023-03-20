from bs4 import BeautifulSoup
import requests
import re
import json
#to send emails
import yagmail 
#store and get variables on my local OS/evn
import os

def compareValue(cur_value):
    if cur_value<-0.10:
        print(f"This is a new value: {cur_value}")
        send_an_email_when_price_went_down()
    else:
        print(f"This is the same value: {cur_value}")
        send_an_email_when_price_is_the_same()

def get_value():
    url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"
    get_content=requests.get(url).text # getting SOURCE CODE 
    json_string = re.search(r"this\.WebMarketData = ({.*?});", get_content).group(1) # chatGPT helped
    data = json.loads(json_string)
    value = data["change_prev_close_percentage"]
    return float(value)


# Comparing this value to -.1 and if it's below than -0.1 send this email
def send_an_email_when_price_went_down():  
    # Setting up email 
    receiver_email= "kgdweavge@emlpro.com" # from https://dropmail.me/en/
    sender_email=os.getenv('email')
    subject="The price has gone DOWN!"
    passw=os.getenv("password")
    content=f"""Hey mate,
    The price has gone and it is {newest_values} 
    """
    #Setting app the app to send email via gmail using smtp protocol
    yag=yagmail.SMTP(user=sender_email,password=passw)
    #Sending the actual email to the receiver
    yag.send(to=receiver_email,subject=subject,contents=content)
    print('E-mail was sent!')

# Comparing this value to -.1 and if it's NOT below than -0.1 send this email
def send_an_email_when_price_is_the_same():  
    # Setting up email 
    receiver_email= "kgdweavge@emlpro.com" # from https://dropmail.me/en/
    sender_email=os.getenv('email')
    passw=os.getenv("password")
    subject="The price has gone DOWN!"
    content=f"""Hey mate,
    Nothing new, the price is the same: {newest_values} 
    """
    #Setting app the app to send email via gmail using smtp protocol
    yag=yagmail.SMTP(user=sender_email,password=passw)
    #Sending the actual email to the receiver
    yag.send(to=receiver_email,subject=subject,contents=content)
    print('E-mail was sent!')

#launch the functions
newest_values=get_value()
compareValue(newest_values)

