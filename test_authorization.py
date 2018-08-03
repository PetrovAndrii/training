# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return True

class test_authorization(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_authorization(self):
        success = True
        wd = self.wd
        wd.get("https://booking-test.mdata.com.ua/")
        wd.find_element_by_css_selector(".mobile-version").click()
        wd.find_element_by_css_selector(".login").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("uz.all.test@gmail.com")
        wd.find_element_by_name("pwd").click()
        wd.find_element_by_name("pwd").clear()
        wd.find_element_by_name("pwd").send_keys("P@ssw0rd")
        wd.find_element_by_name("login").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()