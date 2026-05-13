from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://github.com/login")
time.sleep(3)

# username
user_name = driver.find_element(By.NAME, "login")
user_name.send_keys('akasj123@gmail.com')
time.sleep(2)

# password
psw = driver.find_element(By.NAME, "password")
psw.send_keys('Akash0009')
time.sleep(2)

# sign in
login_btn = driver.find_element(By.NAME, "commit")
login_btn.click()

error=driver.find_element(By.XPATH,"//div[@role='alert']")
print(error.text)
input('press Enter key for close Chrome :')
driver.quit()
