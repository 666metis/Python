from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.XPATH, "//input[@type='number']")

search_input.send_keys("1000")
sleep(1)
search_input.clear()
search_input.send_keys("999")
sleep(1)