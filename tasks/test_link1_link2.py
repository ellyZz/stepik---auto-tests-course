import unittest
from selenium import webdriver
import time

class Test1(unittest.TestCase):
    def test_link1(self):
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            first_name = browser.find_element_by_css_selector(
                "div.first_block &gt; div.form-group.first_class &gt; input")
            first_name.send_keys("Ivan")
            last_name = browser.find_element_by_css_selector(
                "div.first_block &gt; div.form-group.second_class &gt; input")
            last_name.send_keys("Ivanovich")
            email = browser.find_element_by_css_selector("div.first_block &gt; div.form-group.third_class &gt; input")
            email.send_keys("Ivan@")
            button = browser.find_element_by_css_selector("button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_css_selector(
            "div.first_block &gt; div.form-group.first_class &gt; input")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector(
            "div.first_block &gt; div.form-group.second_class &gt; input")
        last_name.send_keys("Ivanovich")
        email = browser.find_element_by_css_selector("div.first_block &gt; div.form-group.third_class &gt; input")
        email.send_keys("Ivan@")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text

if __name__ == "__main__":
    unittest.main()