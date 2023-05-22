from selenium import webdriver

import sys
sys.path.append('./config')
import config as config

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# print (current_url)

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

driver.back()

routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Users')]")))
routes_menu.click()
time.sleep(2)
driver.back()

routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Schedule')]")))
routes_menu.click()
time.sleep(2)
driver.back()

routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Booking')]")))
routes_menu.click()
time.sleep(2)
driver.back()

routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Reporting')]")))
routes_menu.click()
time.sleep(2)
driver.back()

routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Finance')]")))
routes_menu.click()
time.sleep(2)
driver.back()

routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Support center')]")))
routes_menu.click()
time.sleep(2)
driver.back()

routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Review')]")))
routes_menu.click()
time.sleep(2)
driver.back()

routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Profile')]")))
routes_menu.click()
time.sleep(2)
driver.back()

routes_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Setting')]")))
routes_menu.click()



# Keep the browser open
input("Press Enter to close the browser...")

# Close the browser
driver.quit()