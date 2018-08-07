# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def open_mobile_page(self):
        wd = self.wd
        wd.get("https://booking-test.mdata.com.ua/")
        wd.find_element_by_css_selector(".mobile-version").click()


    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_css_selector(".login").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(username)
        wd.find_element_by_name("pwd").click()
        wd.find_element_by_name("pwd").clear()
        wd.find_element_by_name("pwd").send_keys(password)
        wd.find_element_by_name("login").click()


    def login_google(self, username, password):
        wd = self.wd
        wd.find_element_by_css_selector(".login").click()
        wd.find_element_by_css_selector(".google").click()
        wd.switch_to.window(wd.window_handles[1])
        wd.find_element_by_name("identifier").click()
        wd.find_element_by_name("identifier").clear()
        wd.find_element_by_name("identifier").send_keys(username)
        wd.find_element_by_name("identifier").send_keys(Keys.ENTER)
        time.sleep(3)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("password").send_keys(Keys.ENTER)
        time.sleep(3)
        wd.switch_to.window(wd.window_handles[0])

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("/html/body/div[2]/div[1]/span/a").click()
        wd.find_element_by_css_selector(".logout").click()


    def destroy(self):
        self.wd.quit()