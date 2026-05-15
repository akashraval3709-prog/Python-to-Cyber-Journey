from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get('https://www.google.com')

time.sleep(2)

search_box = driver.find_element(By.NAME, 'q')

search_box.send_keys("Cyber Security Road Map 2026")

time.sleep(2)

search_box.send_keys(Keys.ENTER)

input('Press Enter key for close Chrome : ')

driver.quit()
