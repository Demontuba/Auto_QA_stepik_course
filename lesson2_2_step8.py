import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

name_field = browser.find_element(By.CSS_SELECTOR, "input:nth-of-type(1)")
name_field.send_keys("A")
lastname_field = browser.find_element(By.CSS_SELECTOR, "input:nth-of-type(2)")
lastname_field.send_keys("B")
email_field = browser.find_element(By.CSS_SELECTOR, "input:nth-of-type(3)")
email_field.send_keys("A@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(3)