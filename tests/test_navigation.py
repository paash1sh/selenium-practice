# practicing browser navigation with selenium
# back, forward, refresh etc

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# test 1 - basic navigation
print("--- Navigation Test ---")
driver.get("http://the-internet.herokuapp.com")
time.sleep(1)
print("title:", driver.title)

# click a link
link = driver.find_element_by_link_text("Form Authentication")
link.click()
time.sleep(1)
print("navigated to:", driver.current_url)

# go back
driver.back()
time.sleep(1)
print("went back to:", driver.current_url)

# go forward
driver.forward()
time.sleep(1)
print("went forward to:", driver.current_url)

# test 2 - open new tab
# NOTE: tried this but had trouble, will fix later
# driver.execute_script("window.open('');")

# test 3 - page refresh
driver.refresh()
time.sleep(1)
print("page refreshed")

# test 4 - get page source length
source_len = len(driver.page_source)
print("page source length:", source_len)

driver.quit()
print("navigation tests done")
