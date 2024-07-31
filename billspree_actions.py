from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def perform_billspree_actions(driver):
    # Click on the "Packages & Plans" section
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Packages & Plans"]')))
    packages_and_plans = driver.find_element(By.XPATH, '//span[text()="Packages & Plans"]')
    packages_and_plans.click()
    print("Navigated to Packages & Plans")
    time.sleep(3)

    # Click on the caret button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.my-caret-button')))
    package_actions_button = driver.find_element(By.CSS_SELECTOR, 'button.my-caret-button')
    package_actions_button.click()
    print("Opened actions menu for the package")
    time.sleep(3)

    # Click on the "View/Update" action for Billspree
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul#dropdown-basic')))
    billspree_actions = driver.find_elements(By.CSS_SELECTOR, 'ul#dropdown-basic > li.batchActions')
    if len(billspree_actions) > 1:
        billspree_actions[1].click()  # Index 1 corresponds to "View/Update"
        print("Clicked on 'View/Update' action for Billspree.")
    else:
        print("Unable to find the 'View/Update' action for Billspree.")
    time.sleep(3)

    # List of tab names to click on
    tab_names = ["Values", "Components*", "Subscription Properties", "Meter Properties", "Unmeter Usage", "Batches*", "Plans"]

    # Iterate over each tab and click based on index
    for tab_name in tab_names:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div#exTab1 ul.nav.nav-pills.nav-justified > li.nav-item > a.nav-link')))
        nav_tabs = driver.find_elements(By.CSS_SELECTOR, 'div#exTab1 ul.nav.nav-pills.nav-justified > li.nav-item > a.nav-link')
        for tab in nav_tabs:
            if tab.text.strip() == tab_name:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(tab))
                tab.click()
                print(f"Clicked on the {tab_name} tab")
                time.sleep(5)  # Allow time for the UI to update
                break

    # Click on the "View" button in the Plans section
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.table-content-item > button.btn')))
    view_button = driver.find_element(By.CSS_SELECTOR, 'div.table-content-item > button.btn')
    view_button.click()
    print("Clicked on the View button")
    time.sleep(10)
