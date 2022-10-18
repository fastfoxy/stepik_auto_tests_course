import pytest
from selenium.webdriver.common.by import By
import time
import math

pages = ['https://stepik.org/lesson/236895/step/1',\
    'https://stepik.org/lesson/236896/step/1',\
        'https://stepik.org/lesson/236897/step/1',\
            'https://stepik.org/lesson/236898/step/1',\
                'https://stepik.org/lesson/236899/step/1',\
                    'https://stepik.org/lesson/236903/step/1',\
                        'https://stepik.org/lesson/236904/step/1',\
                            'https://stepik.org/lesson/236905/step/1']

@pytest.mark.parametrize('current_link', pages)
def test_guest_should_see_login_link(browser, current_link):
    link = f"{current_link}"
    browser.get(link)
    
    # неявное ожидание появления элементов
    browser.implicitly_wait(10)

    answer_field = browser.find_element(By.CSS_SELECTOR, "textarea.textarea")
    answer = math.log(int(time.time()))
    answer_field.send_keys(str(answer))

    send_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    send_button.click()

    time.sleep(2)

    hint = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    hint_text = hint.text
    print(hint_text)
    assert hint_text == "Correct!"

