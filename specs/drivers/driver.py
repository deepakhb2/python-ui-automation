import sys
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


load_dotenv()

def driver():
    if(os.environ['BROWSER'] == 'chrome'):
        return chrome()
    elif(os.environ['BROWSER'] == 'firefox'):
        return firefox()

def chrome():
    driver_version = os.environ['CHROME_DRIVER_VERSION']
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    if(os.environ['HEADLESS'] == "True"):
        chrome_options.add_argument("--headless")
    return webdriver.Chrome(f'driver/{sys.platform}/chrome/{driver_version}/chromedriver', options=chrome_options)

def firefox():
    options = FirefoxOptions()
    options.log.level = "trace"
    if(os.environ['HEADLESS'] == "True"):
        options.set_headless(headless=True)
    capabilities = DesiredCapabilities().FIREFOX
    binary = FirefoxBinary('/firefox/firefox')
    return webdriver.Firefox(firefox_binary=binary, executable_path = f'driver/{sys.platform}/firefox/geckodriver', options=options, capabilities=capabilities)
