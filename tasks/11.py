from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button1 = browser.find_element_by_css_selector("body > form > div > div > button").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    ans = browser.find_element_by_css_selector("#answer").send_keys(y)
    button2 = browser.find_element_by_css_selector("body > form > div > div > button").click()

finally:
        time.sleep(10)
        browser.quit()