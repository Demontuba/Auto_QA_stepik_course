from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    desire_number = browser.find_element(By.CSS_SELECTOR, "#treasure")
    desire_number_valuex = desire_number.get_attribute("valuex")
    desire_number = calc(desire_number_valuex)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(desire_number)

    check_robot = browser.find_element(By.ID, "robotCheckbox")
    check_robot.click()

    radio_robot = browser.find_element(By.ID, "robotsRule")
    radio_robot.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()
finally:
    time.sleep(5)
    browser.quit()