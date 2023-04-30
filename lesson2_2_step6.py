import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    desire_number = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    field = browser.find_element(By.ID, "answer")
    field.send_keys(desire_number)

    check_robot = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check_robot.click()

    radio_robot = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio_robot.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()