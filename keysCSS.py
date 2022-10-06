
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# lgin on prepbytes

driver = webdriver.Chrome(
    executable_path="C:\SeleniumDrivers\chromedriver.exe")

driver.get("https://www.prepbytes.com/login")
driver.implicitly_wait(20)
emailInput = driver.find_element(By.NAME, 'email_input')
loginBtn = driver.find_element(
    By.CLASS_NAME, 'SignIn__container--right-form--container-middle-form--button')
passwordInput = driver.find_element(By.NAME, 'password_input')

emailInput.send_keys('thapliyalamit2001@gmail.com')
passwordInput.send_keys('Amit@2001')
loginBtn.click()
