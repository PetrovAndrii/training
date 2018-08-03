# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

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
        wd = self.wd
        self.open_mobile_page(wd)
        self.login(wd, username="uz.all.test@gmail.com", password="P@ssw0rd")
        self.logout(wd)


    def open_mobile_page(self, wd):
        wd.get("https://booking-test.mdata.com.ua/")
        wd.find_element_by_css_selector(".mobile-version").click()


    def login(self, wd, username, password):
        wd.find_element_by_css_selector(".login").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(username)
        wd.find_element_by_name("pwd").click()
        wd.find_element_by_name("pwd").clear()
        wd.find_element_by_name("pwd").send_keys(password)
        wd.find_element_by_name("login").click()


    def logout(self, wd):
        wd.find_element_by_xpath("/html/body/div[2]/div[1]/span/a").click()
        wd.find_element_by_css_selector(".logout").click()


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()