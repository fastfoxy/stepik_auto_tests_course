from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_value = browser.find_element(By.ID, "input_value")

    # Посчитать математическую функцию от x (код для этого приведён ниже).
    # Ввести ответ в текстовое поле.
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(str(calc(x_value.text)))
    
     # Нажать на кнопку Submit.
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()