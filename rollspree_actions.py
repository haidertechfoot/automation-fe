from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def perform_rollspree_actions(driver):
    # Click on the caret button in Rollspree
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.my-caret-button')))
    rollspree_actions_button = driver.find_element(By.CSS_SELECTOR, 'button.my-caret-button')
    rollspree_actions_button.click()
    print("Opened actions menu for the Rollspree package")
    time.sleep(3)

    # Click on the "View/Update" action for Rollspree
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul#dropdown-basic')))
    rollspree_actions = driver.find_elements(By.CSS_SELECTOR, 'ul#dropdown-basic > li.batchActions')
    if len(rollspree_actions) > 1:
        rollspree_actions[1].click()  # Index 1 corresponds to "View/Update"
        print("Clicked on 'View/Update' action for Rollspree.")
    else:
        print("Unable to find the 'View/Update' action for Rollspree.")
    time.sleep(3)

    # Ensure the tabs are loaded
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#exTab1 ul.nav.nav-pills.nav-justified')))

    # List of tab names in Rollspree to click on
    rollspree_tab_names = ["Values", "Components*", "Contract Properties", "Time and Attendance Metrics", "Batches*", "Plans"]

    # Iterate over each tab and click based on visible text
    for tab_name in rollspree_tab_names:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#exTab1 ul.nav.nav-pills.nav-justified > li.nav-item > a.nav-link')))
        nav_tabs = driver.find_elements(By.CSS_SELECTOR, 'div#exTab1 ul.nav.nav-pills.nav-justified > li.nav-item > a.nav-link')
        for tab in nav_tabs:
            if tab.text.strip() == tab_name:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(tab))
                tab.click()
                print(f"Clicked on the {tab_name} tab in Rollspree")
                time.sleep(5)  # Allow time for the UI to update
                break

    # Click on the "View" button in the Plans section
    try:
        view_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.table-content-item > button.btn'))
        )
        view_button.click()
        print("Clicked on the View button in the Plans section of Rollspree")
        time.sleep(10)
    except TimeoutException:
        print("View button was not found or not clickable.")
