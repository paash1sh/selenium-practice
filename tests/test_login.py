# my first selenium script
# testing login on a demo site
# learned this from youtube tutorial

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# open browser
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")

time.sleep(2)

# find username and password
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

# type in credentials
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

time.sleep(1)

# click login button
login_btn = driver.find_element_by_css_selector(".fa-sign-in")
login_btn.click()

time.sleep(2)

# check if login worked
message = driver.find_element_by_id("flash")
if "You logged into a secure area" in message.text:
    print("TEST PASSED - login worked!")
else:
    print("TEST FAILED - something went wrong")

driver.quit()
# init
# fix selector
