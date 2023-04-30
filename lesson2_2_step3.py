import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_number = browser.find_element(By.ID, "num1").text
    second_number = browser.find_element(By.ID, "num2").text
    result = int(first_number) + int(second_number)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(3)
finally:
    time.sleep(5)
    browser.quit()