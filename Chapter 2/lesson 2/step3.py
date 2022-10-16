from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Открыть страницу http://suninjuly.github.io/selects1.html
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_value = browser.find_element(By.ID, "num1")
    y_value = browser.find_element(By.ID, "num2")

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(int(x_value.text) + int(y_value.text)))
    
    # Нажать на кнопку Submit.
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # ждем
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()