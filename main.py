from selenium import webdriver
from login import login
from navigation import navigate_to_billspree, navigate_to_rollspree
from billspree_actions import perform_billspree_actions
from rollspree_actions import perform_rollspree_actions
from notification_handler import check_notifications
import time

# Initialize the WebDriver (assuming Chrome)
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

    # Call the notification function after all scheduled processes
    status = None
    while status is None:
        status = check_notifications(driver)
        time.sleep(10)  # Wait and check again if no status is found

    if status:
        print("All processes completed successfully.")
    else:
        print("A process failed. Terminating the script.")
        # Handle failure logic, if necessary

    # Optional: Keep the browser open for a while to observe
    time.sleep(10)

finally:
    # Quit the WebDriver
    driver.quit()
