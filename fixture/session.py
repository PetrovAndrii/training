# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
import time



class SessionHelper:


    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        wd = self.app.wd
        self.app.open_mobile_page()
        if wd.find_elements_by_css_selector(".login"):
            wd.find_element_by_css_selector(".login").click()
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(username)
            wd.find_element_by_name("pwd").click()
            wd.find_element_by_name("pwd").clear()
            wd.find_element_by_name("pwd").send_keys(password)
            wd.find_element_by_name("login").click()
        else:
            pass

    def login_google(self, username, password):
        wd = self.app.wd
        self.app.open_mobile_page()
        if wd.find_elements_by_css_selector(".login"):
            self.google_form(password, username)
        else:
            self.logout()
            self.google_form(password, username)

    def google_form(self, password, username):
        wd = self.app.wd
        wd.find_element_by_css_selector(".login").click()
        wd.find_element_by_css_selector(".google").click()
        wd.switch_to.window(wd.window_handles[1])
        wd.find_element_by_name("identifier").click()
        wd.find_element_by_name("identifier").clear()
        wd.find_element_by_name("identifier").send_keys(username)
        wd.find_element_by_name("identifier").send_keys(Keys.ENTER)
        time.sleep(2)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("password").send_keys(Keys.ENTER)
        time.sleep(2)
        wd.switch_to.window(wd.window_handles[0])

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[2]/div[1]/span/a").click()
        wd.find_element_by_css_selector(".logout").click()