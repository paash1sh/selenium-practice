# testing forms on the-internet demo site
# trying different input types

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

# test text input
driver.get("http://the-internet.herokuapp.com/inputs")
time.sleep(1)

number_input = driver.find_element_by_tag_name("input")
number_input.send_keys("12345")
time.sleep(1)
print("number input test done")

# test dropdown
driver.get("http://the-internet.herokuapp.com/dropdown")
time.sleep(1)

dropdown = Select(driver.find_element_by_id("dropdown"))
dropdown.select_by_visible_text("Option 1")
time.sleep(1)
selected = dropdown.first_selected_option.text
print("selected option:", selected)

if selected == "Option 1":
    print("dropdown test PASSED")
else:
    print("dropdown test FAILED")

# test checkbox
driver.get("http://the-internet.herokuapp.com/checkboxes")
time.sleep(1)

checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()
        print("checked a checkbox")

time.sleep(1)
print("checkbox test done")

driver.quit()
print("all done!")
# forms
# select fix
