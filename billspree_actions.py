import subprocess
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

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="newButton"]')))
    newButton = driver.find_element(By.CSS_SELECTOR, 'button[id="newButton"]')
    newButton.click()
    print("Navigated to Packages & Plans")
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="import-button"]')))
    newButton = driver.find_element(By.CSS_SELECTOR, 'button[id="import-button"]')
    newButton.click()
    print("Navigated to Packages & Plans")
    time.sleep(10)

    subprocess.run('/home/adeel/Documents/selenium/selenium/automation-fe/xdopkg.sh', shell=True)
    time.sleep(3)

    # Wait until the "Save" button is present in the DOM and is clickable
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "save-button"))
    )
    # Click the "Save" button
    save_button.click()
    time.sleep(3)

     # Wait until the "Close" button is present and clickable, then click it
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#modal-btn'))
    )
    close_button.click()
    print("Clicked on the Close button")
    time.sleep(3)

    # Wait until the "Back" button is present and clickable, then click it
    back_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#back-button'))
    )
    back_button.click()
    print("Clicked on the Back button")
    time.sleep(3)

    # Wait until the pagination button for the last page is present and clickable, then click it
    last_page_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="go to last page"]'))
    )
    last_page_button.click()
    print("Clicked on the pagination button to go to the last page")
    time.sleep(3)

    # Wait until the pagination button for the last page is present and clickable, then click it
    last_page_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="go to last page"]'))
    )
    last_page_button.click()
    print("Clicked on the pagination button to go to the last page")
    time.sleep(3)

        # Wait for the last package's caret button and click it
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.my-caret-button'))
    )
    package_actions_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.my-caret-button')
    last_package_action_button = package_actions_buttons[-1]
    last_package_action_button.click()
    print("Opened actions menu for the last package")
    time.sleep(3)

    # Wait for the "Plans" option and click it
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul#dropdown-basic > li.batchActions'))
    )
    actions_menu_items = driver.find_elements(By.CSS_SELECTOR, 'ul#dropdown-basic > li.batchActions')
    plans_action = next((item for item in actions_menu_items if item.text.strip() == "Plans"), None)
    if plans_action:
        plans_action.click()
        print("Clicked on 'Plans' action for the last package.")
    else:
        print("Unable to find the 'Plans' action.")
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="newButton"]')))
    newButton = driver.find_element(By.CSS_SELECTOR, 'button[id="newButton"]')
    newButton.click()
    print("Navigated TO NEW Plans")
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="import-button"]')))
    newButton = driver.find_element(By.CSS_SELECTOR, 'button[id="import-button"]')
    newButton.click()
    print("Navigated to Packages & Plans")
    time.sleep(10)

    subprocess.run('/home/adeel/Documents/selenium/selenium/automation-fe/xdoplan.sh', shell=True)
    time.sleep(3)

    # Wait until the "Save" button is present in the DOM and is clickable
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "save-button"))
    )
    # Click the "Save" button
    save_button.click()
    time.sleep(3)

     # Wait until the "Close" button is present and clickable, then click it
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#modal-btn'))
    )
    close_button.click()
    print("Clicked on the Close button")
    time.sleep(3)

    # Wait until the "Back" button is present and clickable, then click it
    back_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#back-button'))
    )
    back_button.click()
    print("Clicked on the Back button")
    time.sleep(3)

    # Click on the "Contacts" section
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "l1") and text()="Contacts"]'))
    )
    contacts_section = driver.find_element(By.XPATH, '//span[contains(@class, "l1") and text()="Contacts"]')
    contacts_section.click()
    print("Clicked on 'Contacts'")
    time.sleep(3)

    # Click on the "Customers" section
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "l2") and text()="Customers"]'))
    )
    customers_section = driver.find_element(By.XPATH, '//span[contains(@class, "l2") and text()="Customers"]')
    customers_section.click()
    print("Clicked on 'Customers'")
    time.sleep(3)
    
    # Click on the "Import Bulk Data" button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#import-bulk-data'))
    )
    import_bulk_data_button = driver.find_element(By.CSS_SELECTOR, 'button#import-bulk-data')
    import_bulk_data_button.click()
    print("Clicked on 'Import Bulk Data' button")
    time.sleep(3)

    # Execute the script to handle the file selection dialog
    subprocess.run('/home/adeel/Documents/selenium/selenium/automation-fe/xdocustomer.sh', shell=True)
    time.sleep(3)

    # Wait until the "Schedule Process" button is present and clickable, then click it
    schedule_process_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.scheduleBtn'))
    )
    schedule_process_button.click()
    print("Clicked on 'Schedule Process' button")
    time.sleep(3)

    # Wait until the "Close" button is present and clickable, then click it
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#modal-btn'))
    )
    close_button.click()
    print("Clicked on the Close button")
    time.sleep(3)


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
