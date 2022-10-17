import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistrationPages(unittest.TestCase):
    def test_registration_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        element1.send_keys("Имя")

        element2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        element2.send_keys("Фамилия")

        element3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        element3.send_keys("e@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome text not appear")

    def test_registration_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
        element1.send_keys("Имя")

        element2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
        element2.send_keys("Фамилия")

        element3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
        element3.send_keys("e@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome text not appear")

if __name__ == "__main__":
    unittest.main()