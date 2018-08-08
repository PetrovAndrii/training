# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper



class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_mobile_page(self):
        wd = self.wd
        wd.get("https://booking-test.mdata.com.ua/")
        wd.find_element_by_css_selector(".mobile-version").click()


    def destroy(self):
        self.wd.quit()