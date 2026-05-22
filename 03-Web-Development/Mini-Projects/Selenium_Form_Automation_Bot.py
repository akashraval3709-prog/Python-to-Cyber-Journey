from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

wait=WebDriverWait(driver,20)

# ================= USER INPUT =================

first_name = input('Enter First Name : ')
last_name = input('Enter Last Name : ')
email_input = input('Enter Email : ')
phone = input('Enter Mobile Number : ')
dob = input('Enter DOB (Example: 10 Oct 2006) : ')
address_input = input('Enter Address : ')
state_input = input('Enter City (Example: NCR,Uttar,Pradesh,Haryana,Rajasthan tyep any one) : ')
if state_input=='NCR':
    city_input = input('Enter State (Example: Dehli , Gurgaon ,Noida, type any one): ')
elif state_input=='Uttar':
    city_input = input('Enter State (Example: Agra , Lucknow ,Merrut , type any one): ')

# ==============================================

driver.get('https://demoqa.com/automation-practice-form?utm_source=chatgpt.com')

# first name
fname=wait.until(
    EC.visibility_of_element_located((By.ID,"firstName"))
)

fname.send_keys(first_name)

# last name
lname=wait.until(
    EC.visibility_of_element_located((By.ID,"lastName"))
)

lname.send_keys(last_name)

# user Email
email=wait.until(
    EC.visibility_of_element_located((By.ID,"userEmail"))
)

email.send_keys(email_input)

# Gender
Gender=wait.until(
    EC.visibility_of_element_located(
        (By.XPATH,"//label[text()='Male']")
    )
)

Gender.click()

# Mobile Number
number=wait.until(
    EC.visibility_of_element_located((By.ID,"userNumber"))
)

number.send_keys(phone)

# Date Of Birth
brd=wait.until(
    EC.visibility_of_element_located((By.ID,"dateOfBirthInput"))
)

brd.send_keys(dob)

# Sports
Sports=wait.until(
    EC.visibility_of_element_located(
        (By.XPATH,"//label[text()='Sports']")
    )
)

Sports.click()

reading=wait.until(
    EC.visibility_of_element_located(
        (By.XPATH,"//input[@value='2']")
    )
)

reading.click()

music=wait.until(
    EC.visibility_of_element_located(
        (By.XPATH,"//input[@value='3']")
    )
)

music.click()

# Address
address=wait.until(
    EC.visibility_of_element_located((By.ID,"currentAddress"))
)

address.send_keys(address_input)

# State
state=wait.until(
    EC.visibility_of_element_located(
        (By.ID,"react-select-3-input")
    )
)

state.send_keys(state_input)
state.send_keys(Keys.ENTER)

# City
city=wait.until(
    EC.visibility_of_element_located(
        (By.ID,"react-select-4-input")
    )
)

city.send_keys(city_input)
city.send_keys(Keys.ENTER)

# Submit Button
submit = wait.until(
    EC.presence_of_element_located((By.ID, "submit"))
)

# Scroll to submit button
driver.execute_script("arguments[0].scrollIntoView(true);", submit)

time.sleep(1)

# JavaScript click
driver.execute_script("arguments[0].click();", submit)



time.sleep(1)

time.sleep(2)

texts= wait.until(
    EC.visibility_of_element_located(
        (By.ID,"example-modal-sizes-title-lg")
    )
)

print(texts.text)

# Close Popup
close_btn = wait.until(
    EC.presence_of_element_located(
        (By.ID,"closeLargeModal")
    )
)

driver.execute_script("arguments[0].click();", close_btn)

print("Popup Closed Successfully ✅")



input('Press Enter key for close Chrome : ')

driver.quit()
