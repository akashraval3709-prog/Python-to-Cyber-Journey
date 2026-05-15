from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
wait=WebDriverWait(driver,10)

try:
  button=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Start']")))
  button.click()
  finish_element=wait.until(EC.visibility_of_element_located((By.ID,"finish")))
  print("Result Text is:", finish_element.text)
  input('press Enter key for close Chrome :')
    
  driver.quit()
except TimeoutException:
    print('Timeout')
