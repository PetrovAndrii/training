# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper



class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_mobile_page(self):
        wd = self.wd
        wd.get("https://booking-test.mdata.com.ua/")
        if (wd.find_elements_by_css_selector(".mobile-version")):
            wd.find_element_by_css_selector(".mobile-version").click()
            wd.execute_script("document.cookie='_uz_emu_on=__on__; path=/; expires=Sun, 01-Jan-2045 00:00:00 GMT'")



    def destroy(self):
        self.wd.quit()