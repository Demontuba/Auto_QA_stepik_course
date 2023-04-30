from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import  math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    desire_number = browser.find_element(By.ID, "input_value")
    x = desire_number.text
    desire_number = calc(x)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(desire_number)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()