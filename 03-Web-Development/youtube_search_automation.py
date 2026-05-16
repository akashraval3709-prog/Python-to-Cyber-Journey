from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(
    service=Service(
          ChromeDriverManager().install()
        )
    )

driver.get('https://www.youtube.com')
print(driver.title)
time.sleep(3)

search_box=driver.find_element(By.NAME,"search_query")
search_box.send_keys('js play list by chai or code ')
time.sleep(2)
submit=driver.find_element(By.XPATH,"//button[@title=\"Search\"]")
submit.click()
input('press Enter key for close Chrome :')
driver.quit()
