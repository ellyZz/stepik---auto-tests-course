from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    img = browser.find_element_by_css_selector("#treasure")
    value = img.get_attribute("valuex")
    y = calc(value)
    ans = browser.find_element_by_css_selector("#answer")
    ans.send_keys(y)

    check = browser.find_element_by_css_selector("#robotCheckbox")
    check.click()

    check1 = browser.find_element_by_css_selector("#robotsrule")
    check1.click()

    button = browser.find_element_by_css_selector("body > div.container > form > div > div > button")
    button.click()

finally:
        time.sleep(10)
        browser.quit()