import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver_path="C:/Users/Pabitha/PycharmProjects/chromedriver.exe"
os.environ["PATH"] += os.pathsep+os.path.dirname(driver_path)
# Create a ChromeOptions object
chrome_options = Options()

# Add experimental option
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver with ChromeOptions
chr_driver = webdriver.Chrome(options=chrome_options)
chr_driver.get("https://www.saucedemo.com/")
chr_driver.maximize_window()
# before
print(chr_driver.get_cookies())
val=chr_driver.find_element(By.ID,"user-name")
val.send_keys("standard_user")
# val.click()
# password
val=chr_driver.find_element(By.ID,"password")
val.send_keys("secret_sauce")
val=chr_driver.find_element(By.ID,"login-button")
val.click()
# Before
time.sleep(2)
print(chr_driver.get_cookies())
# time.sleep(4)
# react-burger-menu-btn
val=chr_driver.find_element(By.ID,"react-burger-menu-btn").click()
# val= chr_driver.find_element(By.XPATH,'//*[@id="logout_sidebar_link"]').click()
logout_button = WebDriverWait(chr_driver, 10).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
logout_button.click()
# After
time.sleep(2)
print(chr_driver.get_cookies())





