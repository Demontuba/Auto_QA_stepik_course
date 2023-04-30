from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
 
link = "http://suninjuly.github.io/find_link_text"
 
try:
    browser = webdriver.Chrome()
    browser.get(link)

    link_number = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link_path = browser.find_element(By.LINK_TEXT, link_number)
    link_path.click()

    txtarea_1 = browser.find_element(By.CSS_SELECTOR, ".container div:nth-of-type(1) input")
    txtarea_1.send_keys("Aleksandr")
    txtarea_2 = browser.find_element(By.CSS_SELECTOR, ".container div:nth-of-type(2) input")
    txtarea_2.send_keys("Zakurin")
    txtarea_3 = browser.find_element(By.CSS_SELECTOR, ".container div:nth-of-type(3) input")
    txtarea_3.send_keys("Kirishi")
    txtarea_4 = browser.find_element(By.CSS_SELECTOR, ".container div:nth-of-type(4) input")
    txtarea_4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
 
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
                                      
# не забываем оставить пустую строку в конце файла
