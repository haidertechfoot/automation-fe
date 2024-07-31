from selenium import webdriver
from login import login
from navigation import navigate_to_billspree, navigate_to_rollspree
from billspree_actions import perform_billspree_actions
from rollspree_actions import perform_rollspree_actions
import time

driver = webdriver.Chrome()

try:
    # Login
    login(driver)

    # Navigate to Billspree and perform actions
    navigate_to_billspree(driver)
    perform_billspree_actions(driver)

    # Navigate to Rollspree and perform actions
    navigate_to_rollspree(driver)
    perform_rollspree_actions(driver)

    time.sleep(10)  # Keep the browser open for a while to observe

finally:
    driver.quit()
