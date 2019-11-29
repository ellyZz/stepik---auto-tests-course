from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 200);")
    ans = browser.find_element_by_css_selector("#answer")
    ans.send_keys(y)
    check = browser.find_element_by_css_selector("#robotCheckbox").click()
    radio = browser.find_element_by_css_selector("#robotsRule").click()
    button = browser.find_element_by_css_selector("body > div.container > form > button").click()

finally:
        time.sleep(5)
        browser.quit()