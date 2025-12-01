from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
chrome_options.add_argument("--guest")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-dev-shm-usage')

URL = 'https://www.saucedemo.com/'

def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    time.sleep(2)
    return driver
