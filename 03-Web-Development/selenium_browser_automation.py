from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

sites=["https://www.google.com",
       "https://www.python.org",
       "https://www.github.com",
       "https://www.kali.org",
       "https://www.hackerrank.com"]

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
for i in sites:
    driver.get(i)
    print(driver.title)
    print(driver.current_url)
    time.sleep(3)
input('press Enter key for close Chrome :')
driver.quit()
