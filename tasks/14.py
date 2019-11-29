from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link  = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    price = WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_css_selector("#book")
    button.click()
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    ans = browser.find_element_by_css_selector("#answer").send_keys(y)
    button2 = browser.find_element_by_css_selector("body > form > div > div > button").click()


finally:
    time.sleep(200)
    browser.quit()