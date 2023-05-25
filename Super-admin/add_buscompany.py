from selenium import webdriver

import sys
sys.path.append('./config')
import config as config

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time

# Replace the path with the path to your Chrome driver
driver = webdriver.Chrome('/drivers/chromedriver')

# maximize the browser window
driver.maximize_window()

# Open the website
driver.get(config.url_superadmin)

# Find the email and password fields and enter your credentials
email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']")))
email_field.send_keys("superadmin@gmail.com")

password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
password_field.send_keys('Password@1234')

button = driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedPrimary")
button.click()

# Wait for the page to load
time.sleep(5)

# get the current URL of the web page
current_url = driver.current_url

# check if the URL contains the expected text (in this case, "/dashboard")
if "dashboard" in current_url:
    print("Successfully redirected to dashboard page.")
else:
    print("Error: failed to redirect to dashboard page.")

# clicking  menus
wait = WebDriverWait(driver, 10)
routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Bus companies')]")))
routes_menu.click()

time.sleep(2)

# Find the button element by class name and text
button = driver.find_element(By.XPATH, "//button[contains(@class, 'MuiButton-root') and span[text()='Add bus company']]")
button.click()

#fill the form
input_element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Bus Legal Name']")
input_element.send_keys("Agni Travels")

input_element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Bus Name...']")
input_element.send_keys("Agni bus")

input_element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter address']")
input_element.send_keys("Kathmandu")

input_element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Contact name']")
input_element.send_keys("Gopal raj")

input_element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Your Email']")
input_element.send_keys("rarin19525@glumark.com")

input_element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='1 (702) 123-4567']")
input_element.send_keys("987658742")

#Input Telephone number
input_element = driver.find_elements(By.CSS_SELECTOR, "input[placeholder='1 (702) 123-4567']")
# Check if there is a second input element
if len(input_element) >= 2:
    # Select the second input element
    input_element = input_element[1]

    # Send keys to the input field
    input_element.send_keys("987895625")
else:
    print("No second input element found")

# #click Bus image button
# wait = WebDriverWait(driver, 10)
# buttons = driver.find_elements(By.CSS_SELECTOR, "span.MuiButton-label")
# button_index = 4 # Replace with the desired index of the button
# if button_index < len(buttons):
#     # Click the button at the desired index
#     buttons[button_index].click()
    
# #select Bus image button
wait = WebDriverWait(driver, 10)
buttons = driver.find_elements(By.CSS_SELECTOR, "span.MuiButton-label")
button_index = 4  # Replace with the desired index of the first button

if button_index < len(buttons):
    # Click the first button at the desired index using JavaScript click event
    # driver.execute_script("arguments[0].click();", buttons[button_index])

    # Find all file input elements
    file_inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='file']")))
    file_path1 = "C:/Users/Lenovo/aaa.jpg"  # Replace with the actual file path for the first file
    file_inputs[0].send_keys(file_path1)

else:
    print("No button found")

#select company logo.
wait = WebDriverWait(driver, 10)
buttons2 = driver.find_elements(By.CSS_SELECTOR, "span.MuiButton-label")
button_index2 = 5  # Replace with the desired index of the second button

if button_index2 < len(buttons2):
    # Click the second button at the desired index using JavaScript click event
    # driver.execute_script("arguments[0].click();", buttons[button_index2])

    # Find all file input elements
    file_inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='file']")))
    file_path2 = "C:/Users/Lenovo/bbb.jpg"  # Replace with the actual file path for the second file
    file_inputs[1].send_keys(file_path2)

else:   
    print("No button found")


input_element = driver.find_element(By.XPATH, '//input[@aria-invalid="false" and @type="number"]')
input_element.send_keys("42")

button_cancel = driver.find_element(By.XPATH, "//button[contains(@class, 'MuiButton-root') and span[text()='Cancel']]")
# Click on the button
button_cancel.click()

#  Keep the browser open 
input("Press Enter to close the browser...")

# Close the browser
driver.quit()