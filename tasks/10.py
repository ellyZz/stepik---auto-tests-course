from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    first_name = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(2)")
    first_name.send_keys("test")
    last_name = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(4)")
    last_name.send_keys("test1")
    email = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(6)")
    email.send_keys("test@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file_add = browser.find_element_by_css_selector("#file")
    file_add.send_keys(file_path)
    button = browser.find_element_by_css_selector("body > div > form > button").click()
finally:
        time.sleep(10)
        browser.quit()