import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['Path']+=r"C:\SeleniumDrivers"

driver = webdriver.Chrome()

#Targeting a url

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(3) # waiting for 3s for web page to download
fireDownload = driver.find_element(By.CSS_SELECTOR,"#downloadButton")
fireDownload.click()
# show text of progress label

#progressLabel = driver.find_element(By.CLASS_NAME,'progress-label')
#print(f"{progressLabel.text}")


# using explicitly wait to wait for the downloaded text as "completed"

WebDriverWait(driver,timeout=30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME,'progress-label'),#element filtration
        'Complete!'# The expected text
    )
)

