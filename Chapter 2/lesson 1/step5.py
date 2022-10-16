from msilib.schema import RadioButton
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу https://suninjuly.github.io/math.html.
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x.
    x_value = browser.find_element(By.ID, "input_value")

    # Посчитать математическую функцию от x (код для этого приведён ниже).
    # Ввести ответ в текстовое поле.
    input_field = browser.find_element(By.CSS_SELECTOR, ".form-control:required")
    input_field.send_keys(str(calc(x_value.text)))
    
    # Отметить checkbox "I'm the robot".
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    
    # Выбрать radiobutton "Robots rule!".
    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()

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