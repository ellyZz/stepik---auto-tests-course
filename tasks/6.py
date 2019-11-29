from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    ans = browser.find_element_by_css_selector("#answer")
    ans.send_keys(y)

    check = browser.find_element_by_css_selector("[for='robotCheckbox']")
    check.click()

    check1 = browser.find_element_by_css_selector("[value='robots']")
    check1.click()

    button = browser.find_element_by_css_selector("body > div.container > form > button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()