from selenium import webdriver
import time

try:
    # http://suninjuly.github.io/registration2.html - 2ая ссылка
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
    last_name.send_keys("Ivanovich")
    email = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
    email.send_keys("Ivan@")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()