from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def navigate_to_billspree(driver):
    # Open the sidebar
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i#menuBtn')))
    menu_button = driver.find_element(By.CSS_SELECTOR, 'i#menuBtn')
    menu_button.click()
    time.sleep(3)

    # Click on the Billspree menu item
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Billspree"]')))
    billspree_menu_item = driver.find_element(By.XPATH, '//span[text()="Billspree"]')
    billspree_menu_item.click()
    print("Navigated to Billspree")
    time.sleep(3)

def navigate_to_rollspree(driver):
    # Click on the "Dashboard" menu item
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Dashboard"]')))
    dashboard_menu_item = driver.find_element(By.XPATH, '//span[text()="Dashboard"]')
    dashboard_menu_item.click()
    print("Navigated to Dashboard")
    time.sleep(15)

    # Click on the "Rollspree" menu item
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Rollspree"]')))
    rollspree_menu_item = driver.find_element(By.XPATH, '//span[text()="Rollspree"]')
    rollspree_menu_item.click()
    print("Navigated to Rollspree")
    time.sleep(4)
