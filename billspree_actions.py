import subprocess
from tkinter.tix import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def perform_billspree_actions(driver):
    # Click on the "Packages & Plans" section
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Packages & Plans"]')))
    packages_and_plans = driver.find_element(By.XPATH, '//span[text()="Packages & Plans"]')
    packages_and_plans.click()
    print("Navigated to Packages & Plans")
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

    try:
        # Check for the presence of pagination controls
        pagination_present = False
        try:
            pagination_buttons = driver.find_elements(By.CSS_SELECTOR, 'a[aria-label="go to last page"]')
            if pagination_buttons:
                pagination_present = True
        except Exception as e:
            print(f"Error checking pagination: {e}")

        if pagination_present:
            try:
                # Click the pagination button to go to the last page
                last_page_button = pagination_buttons[-1]
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(last_page_button))
                last_page_button.click()
                print("Clicked on the pagination button to go to the last page.")
                time.sleep(3)  # Wait for the last page to load
            except Exception as e:
                print(f"Error clicking pagination button: {e}")
        else:
            print("No pagination present. Working with current page packages.")

        # Wait for the package action buttons to be present and visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.my-caret-button'))
        )
        package_actions_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.my-caret-button')

        if package_actions_buttons:
            print(f"Found {len(package_actions_buttons)} package action buttons.")
            last_package_action_button = package_actions_buttons[-1]

            # Ensure the last package action button is clickable
            driver.execute_script("arguments[0].scrollIntoView(true);", last_package_action_button)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(last_package_action_button))
            last_package_action_button.click()
            print("Opened actions menu for the last package.")
        else:
            print("No package action buttons found.")

        time.sleep(3)  # Optional: wait for any resulting actions to complete
        
    except Exception as e:
        print(f"An error occurred while processing the last package action: {e}")


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

    try:
        # Wait for the "Subscriptions" menu item to be clickable and then click it
        subscriptions_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Subscriptions"]'))
        )
        subscriptions_menu.click()
        print("Clicked on the 'Subscriptions' menu item.")
    except Exception as e:
        print(f"An error occurred while clicking on 'Subscriptions': {e}")

    time.sleep(2)

    # Click on the "Import Bulk Data" button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#import-bulk-data'))
    )
    import_bulk_data_button = driver.find_element(By.CSS_SELECTOR, 'button#import-bulk-data')
    import_bulk_data_button.click()
    print("Clicked on 'Import Bulk Data' button")
    time.sleep(3)

    subprocess.run('/home/adeel/Documents/selenium/selenium/automation-fe/xdosubs.sh', shell=True)
    time.sleep(3)

    try:
        # Wait until the modal content with the service list is present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'modal-content'))
        )

        # Locate all the elements with the class name 'service'
        services = driver.find_elements(By.CLASS_NAME, 'service')
        
        if services:
            # Click on the last service in the list
            last_service = services[-1]
            last_service.click()
            print(f"Selected the last service: {last_service.text}")
        else:
            print("No services found in the list.")
            
    except Exception as e:
        print(f"An error occurred while selecting the last package: {e}")

    time.sleep(2)

    # Click on the "Billing Operations" menu item
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Billing Operations"]')))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Billing Operations"]')))
        billing_operations_item = driver.find_element(By.XPATH, '//span[text()="Billing Operations"]')
        billing_operations_item.click()
        print("Navigated to Billing Operations")
    except Exception as e:
        print(f"Error navigating to Billing Operations: {e}")
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="newButton"]')))
    newButton = driver.find_element(By.CSS_SELECTOR, 'button[id="newButton"]')
    newButton.click()
    print("Navigated to Packages & Plans")
    time.sleep(1)

     # Wait for the dropdown to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'select.form-control.contentB')))
    
    # Locate the dropdown element
    dropdown = driver.find_element(By.CSS_SELECTOR, 'select.form-control.contentB')
    
    # Initialize the Select object with the dropdown element
    select = Select(dropdown)
    
    # Select the last option
    select.select_by_index(len(select.options) - 1)
    
    # Print the selected option
    print(f"Selected option: {select.options[-1].text}")
    time.sleep(3)  # Wait for 3 seconds to observe the action

    try:
        # Wait for the "Start Process" button to be present and clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'startProcess')))
        
        # Locate the "Start Process" button
        start_process_button = driver.find_element(By.ID, 'startProcess')
        
        # Click the "Start Process" button
        start_process_button.click()
        
        print("Clicked on 'Start Process' button")
        time.sleep(3)  # Wait for 3 seconds to observe the action
    except Exception as e:
        print(f"Error clicking on 'Start Process' button: {e}")

    # Wait until the "Close" button is present and clickable, then click it
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#modal-btn'))
    )
    close_button.click()
    print("Clicked on the Close button")
    time.sleep(3)

    try:
        # Open the notification bell
        notification_bell = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.notification-icon .fa-bell'))
        )
        notification_bell.click()
        print("Opened the notification bell.")
        time.sleep(2)  # Wait for the notifications to load

        # Check and print counts
        pending_count = int(driver.find_element(By.ID, 'count0').text)
        working_count = int(driver.find_element(By.ID, 'count1').text)
        done_count = int(driver.find_element(By.ID, 'count2').text)
        failed_count = int(driver.find_element(By.ID, 'count3').text)
        print(f"Pending: {pending_count}, Working: {working_count}, Done: {done_count}, Failed: {failed_count}")

        # Click on "Pending" tab and process notifications
        pending_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'tabP'))
        )
        pending_tab.click()
        print("Switched to 'Pending' tab.")
        time.sleep(2)  # Allow time for the tab to load
        # Process notifications in Pending tab (implement specific logic as needed)

        # Click on "Working" tab and process notifications
        working_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'tabW'))
        )
        working_tab.click()
        print("Switched to 'Working' tab.")
        time.sleep(2)  # Allow time for the tab to load
        # Process notifications in Working tab (implement specific logic as needed)

        # Click on "Done" tab and process notifications
        done_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'tabD'))
        )
        done_tab.click()
        print("Switched to 'Done' tab.")
        time.sleep(2)  # Allow time for the tab to load
        # Process notifications in Done tab (implement specific logic as needed)

        # Click on "Failed" tab and process notifications
        failed_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'tabF'))
        )
        failed_tab.click()
        print("Switched to 'Failed' tab.")
        time.sleep(2)  # Allow time for the tab to load
        # Process notifications in Failed tab (implement specific logic as needed)

        # Close the notification bell (if there's a specific way to do this, add it here)
        # Example: Clicking outside the notification area or a close button
        # close_button = driver.find_element(By.CSS_SELECTOR, 'CSS_SELECTOR_FOR_CLOSE_BUTTON')
        # close_button.click()
        print("Closed the notification bell.")

    except Exception as e:
        print(f"An error occurred while managing notifications: {e}")

    time.sleep(2)
    

    # Open the dropdown
    try:    
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'select.form-control'))
        )
        dropdown.click()
        print("Opened the dropdown menu.")
        time.sleep(1)  # Give it a moment to open

        # Locate all options within the dropdown
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'select.form-control option'))
        )

        if options:
            print(f"Found {len(options)} options.")
            # Click on the last option
            last_option = options[-1]
            driver.execute_script("arguments[0].scrollIntoView(true);", last_option)  # Scroll to the last option
            last_option.click()
            print("Selected the last package name.")
        else:
            print("No options found in the dropdown.")
    except Exception as e:
        print(f"An error occurred while selecting the package: {e}")
    time.sleep(3)

    try:
        # Wait until the "Meters" option is clickable and then click it
        meters_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Meters-id'))
        )
        meters_option.click()
        print("Clicked on the 'Meters' option.")
    except Exception as e:
        print(f"An error occurred while clicking on the 'Meters' option: {e}")
    time.sleep(2)

     # Open the dropdown
    try:    
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'select.form-control'))
        )
        dropdown.click()
        print("Opened the dropdown menu.")
        time.sleep(1)  # Give it a moment to open

        # Locate all options within the dropdown
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'select.form-control option'))
        )

        if options:
            print(f"Found {len(options)} options.")
            # Click on the last option
            last_option = options[-1]
            driver.execute_script("arguments[0].scrollIntoView(true);", last_option)  # Scroll to the last option
            last_option.click()
            print("Selected the last package name.")
        else:
            print("No options found in the dropdown.")

    except Exception as e:
        print(f"An error occurred while selecting the package: {e}")
    
    time.sleep(5)


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
