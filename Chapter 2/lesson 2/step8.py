from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']:required")
    element1.send_keys("Имя")

    element2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']:required")
    element2.send_keys("Фамилия")

    element3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']:required")
    element3.send_keys("e@mail.ru")

    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'file.txt')

    element4 = browser.find_element(By.CSS_SELECTOR, "#file:required")
    element4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()