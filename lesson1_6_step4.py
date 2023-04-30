from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
link = "http://suninjuly.github.io/simple_form_find_task.html"
 
try:
    browser = webdriver.Chrome()
    browser.get(link)
 
    name_field = browser.find_element(By.CSS_SELECTOR, ".container div:nth-of-type(1) input")
    name_field.send_keys("Aleksandr")
    lastname_field = browser.find_element(By.CSS_SELECTOR, ".container div:nth-of-type(2) input")
    lastname_field.send_keys("Zakurin")
    city_field = browser.find_element(By.CSS_SELECTOR, ".container div:nth-of-type(3) input")
    city_field.send_keys("Kirishi")
    country_field = browser.find_element(By.CSS_SELECTOR, ".container div:nth-of-type(4) input")
    country_field.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "#submit_button")
    button.click()
 
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
                                      
# не забываем оставить пустую строку в конце файла
