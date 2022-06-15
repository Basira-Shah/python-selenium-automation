from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/ahmadshah/Desktop/automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')

# By multiple classes  # Logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

# By one class  # Create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# By attribute  # Your name
driver.find_element(By.CSS_SELECTOR, "input[type=text]")

# By attribute  # Email
driver.find_element(By.CSS_SELECTOR, "input[type=email]")

# By attribute  # Password
driver.find_element(By.CSS_SELECTOR, "input[type=password]")

# By Xpath using multiple nodes  # Password must be at least 6 character
driver.find_element(By.XPATH, "//div[@class='a-box a-alert-inline a-alert-inline-info auth-inlined-information-message a-spacing-top-mini']/div/div")

# By attribute  #  Re enter password
driver.find_element(By.CSS_SELECTOR, "input[type=password]")

# By ID  # Create your Amazon account
driver.find_element(By.ID, 'createAccountSubmit')

# By attribute  #  Condition of use
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# By attribute  # Privacy and notice
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

# By partial attribute # Sign in
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin']")




