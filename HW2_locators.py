from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/ahmadshah/Desktop/automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')

# By Xpath # Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# By ID  # Email field
driver.find_element(By.ID, 'ap_email')

# By ID  # Continue button
driver.find_element(By.ID, 'continue')

# By Xpath using partial attributes # Privacy notice
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")

# Conditions of use
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
# By multiple nodes,    # condition of use
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'ap_signin_notification_condition_of_use')]")

# By Xpath # Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# By ID # Forgot password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# By ID  # Create your Amazon account
driver.find_element((By.ID, 'createAccountSubmit'))

# By ID  # Other issues with sign-in
driver.find_element(By.ID, 'ap-other-signin-issues-link')



