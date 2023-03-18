# web for scarping - https://automated.pythonanywhere.com/tours/

### -> In this case we have some data that keeps changing/updating <- ###

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# We need to import the Keys lib too
from selenium.webdriver.common.keys import Keys
from time import gmtime, strftime # since the contect keeps changing each a few sec
import time
#to bypass certicate error I used this command -> xattr -d com.apple.quarantine chromedriver
service = Service('/Users/rock/Documents/scripts/python/udemy/webscraping/chromedriver_mac64/chromedriver')
#Urls
home="https://automated.pythonanywhere.com"
login="https://automated.pythonanywhere.com/login/"

def get_driver():
    # Configure the browser instance
    options = webdriver.ChromeOptions()
    #This method,add_argument allows you to add a command-line argument to the browser instance
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized") #Starts the browser maximized, regardless of any previous settings
    #options.add_argument("disable-dev-shm-usage") # for VM partition and is too small in certain VM environments, causing Chrome to fail or crash 
    options.add_argument("no-sandbox") #Disables the sandbox for all process types that are normally sandboxed. Meant to be used as a browser-level switch for testing purposes only
    options.add_argument("disable-blink-features") #Disable one or more Blink runtime-enabled features. 
    #This method, add_experimental_option allows you to add an experimental option to the browser instance. 
    
    #Experimental options are options that are not officially supported by the browser vendor, but can still be used to tweak the browser behavior.
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) #Enable indication that browser is controlled by automation

    driver=webdriver.Chrome(service=service,options=options)
    driver.get(login)
    return driver

#fn1 - just get numbers
def noTxt(text):
    numbers=float(text.split(": ")[1])
    return numbers

#fn2 - create a new file and save a new value
def writeFile(text):
    fileName=strftime("%Y-%m-%d_%H:%M:%S", gmtime())+".txt"
    with open(fileName, "w") as file:
        file.write(text)

def autoLogin():
    #navigate to a webpage
    driver=get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated") # "by" is casesensetive
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.ENTER) # click enter/return
    #We gonna loop forever here this open browser
    while True:
        time.sleep(2)
        element =driver.find_element(by="xpath", value="/html/body/div[1]/h1[2]")
        text=str(noTxt(element.text))
        writeFile(text)

autoLogin()