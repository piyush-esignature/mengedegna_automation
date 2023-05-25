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
routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Users')]")))
routes_menu.click()

time.sleep(2)

# Find the button element by class name and text
button = driver.find_element(By.XPATH, "//button[contains(@class, 'MuiButton-root') and span[text()='+']]")
button.click()

#fill the form
input_element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter First Name']")
input_element.send_keys("Robin")

input_element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Last Name']")
input_element.send_keys("Charm")

input_element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Your Email']")
input_element.send_keys("sachintendulkar@usa.com")

input_element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='1 (702) 123-4567']")
input_element.send_keys("987658742")

# #checkbox selection.
# checkbox = driver.find_element(By.CLASS_NAME, "jss1320")
# is_checked = checkbox.is_selected()

# if not is_checked:
#     checkbox.click()





#  Keep the browser open 
input("Press Enter to close the browser...")

# Close the browser
driver.quit()