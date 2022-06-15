from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/ahmadshah/Desktop/automation/python-selenium-automation/chromedriver')
driver.get('https://www.amazon.com/')

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")

# By classes
# By 1 class
driver.find_element(By.CSS_SELECTOR, "span.icp-nav-flag-us")
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag-us")  # here you can omit the tag
# By multiple class
driver.find_element(By.CSS_SELECTOR, "span.icp-nav-flag.icp-nav-flag-us")
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")  # here too

# By other attributes
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "[data-csa-c-content-id='nav_cs_bestsellers']")  # not tag
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers'][data-csa-c-content-id='nav_cs_bestsellers']")

# By class and attributes
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers']")  # here you combine attribute with class
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers'].nav-a")

# By ID and attributes
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox[name='field-keywords']")   # we are not using them too much because id areunique no need for other attributes

# By partial attribute
driver.find_element(By.CSS_SELECTOR, '[href*="ap_signin_notification_privacy_notice"]')
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_privacy_notice']")


# By parent and child elements (parent through child not any other order as xpath)
driver.find_element(By.CSS_SELECTOR, '#legalTextRow [href*="ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496"]')
driver.find_element(By.CSS_SELECTOR, 'div.a-section#legalTextRow [href*="ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496"]')
driver.find_element(By.CSS_SELECTOR, 'div.a-section [href*="ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496"]')














