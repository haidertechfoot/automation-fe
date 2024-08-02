from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    driver.get("https://stage.billspree.work")
    
    # Wait for the login form to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="email"]')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="password"]')))

    # Locate the email and password fields and the login button
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[id="email"]')
    password_field = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
    login_button = driver.find_element(By.CSS_SELECTOR, 'div#signIn')

    # Enter your login credentials
    email_field.send_keys('stage@gmail.com')
    password_field.send_keys('abc123')

    # Click the login button
    login_button.click()
    
    # Wait for the login process to complete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[id="base_node"]')))
    print("Logged in successfully")
