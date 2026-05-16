from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)
driver.get('https://the-internet.herokuapp.com/javascript_alerts')

time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
time.sleep(2)

alert1=driver.switch_to.alert
time.sleep(2)
alert1.accept()

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(2)
alert2=driver.switch_to.alert
time.sleep(2)
alert2.dismiss()

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
time.sleep(2)

alert3=driver.switch_to.alert
time.sleep(2)
alert3.send_keys('Akash')
time.sleep(2)
alert3.accept()


time.sleep(4)
driver.quit()   aa mukyo che me 
