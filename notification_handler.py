from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def check_notifications(driver):
    try:
        # Open the notification bell
        notification_bell = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.notification-icon .fa-bell'))
        )
        notification_bell.click()
        print("Opened the notification bell.")
        time.sleep(2)  # Wait for the notifications to load

        # Check the counts
        done_count = int(driver.find_element(By.ID, 'count2').text)
        failed_count = int(driver.find_element(By.ID, 'count3').text)
        print(f"Done: {done_count}, Failed: {failed_count}")

        # Check if there are any failures
        if failed_count > 0:
            print("Process failed. Stopping further execution.")
            return False

        # Check if any process is done
        if done_count > 0:
            print("Process completed successfully. Proceeding to the next.")
            return True

        return None  # No update yet, continue waiting

    except Exception as e:
        print(f"An error occurred while checking notifications: {e}")
        return None
