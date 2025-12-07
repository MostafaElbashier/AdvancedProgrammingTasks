from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Web Scraping")
search_box.send_keys(Keys.RETURN)

time.sleep(2)  
print("Page Title:", driver.title)

driver.quit()