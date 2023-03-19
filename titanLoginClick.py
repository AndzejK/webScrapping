from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
#to bypass certicate error I used this command -> xattr -d com.apple.quarantine chromedriver
service = Service('/Users/rock/Documents/scripts/python/udemy/webscraping/chromedriver_mac64/chromedriver')
website="https://titan22.com/"
#Xpaths:

"""Settings of the browser"""
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
    driver.get(website)
    return driver

login="andrewLrubowec@gma1l.com"
password="qwertyu10"
xpath="/html/body/header/div[1]/div[1]/div/div[3]/a[2]"

def main():
    #navigate to a webpage
    driver=get_driver()
    #Find login/account element/button by xpath and click on it 
    driver.find_element(by="xpath", value=xpath).click()
    driver.find_element(by="id", value="CustomerEmail").send_keys(login) # "by" is casesensetive
    driver.find_element(by="id", value="CustomerPassword").send_keys(password + Keys.ENTER) # click enter/return
    time.sleep(20)
    return driver

# They have capture against bots :(

print(main())


