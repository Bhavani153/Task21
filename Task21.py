import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username=driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("standard_user")
time.sleep(2)
password=driver.find_element(By.ID,"password")
password.click()
password.send_keys("secret_sauce")
time.sleep(2)

sauccookies=driver.get_cookies()
print("cookies created before login:",sauccookies)
login=driver.find_element(By.ID,"login-button")
login.click()
sauccookies=driver.get_cookies()
print("cookies created after login:",sauccookies)
driver.find_element(By.ID,'react-burger-menu-btn').click()
time.sleep(2)
driver.find_element(By.ID,"logout_sidebar_link").click()


