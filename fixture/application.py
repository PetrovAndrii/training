# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from fixture.session import SessionHelper
import time


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)


    def open_mobile_page(self):
        wd = self.wd
        wd.get("https://booking-test.mdata.com.ua/")
        wd.find_element_by_css_selector(".mobile-version").click()


    def search_train(self, group_stations):
        wd = self.wd
        wd.find_element_by_name("from-title").click()
        wd.find_element_by_css_selector(".ui-autocomplete-input").click()
        wd.find_element_by_css_selector(".ui-autocomplete-input").clear()
        wd.find_element_by_css_selector(".ui-autocomplete-input").send_keys(group_stations.from_station)
        wd.find_element_by_css_selector(".ui-autocomplete-input").send_keys(Keys.ENTER)
        wd.find_element_by_name("to-title").click()
        wd.find_element_by_css_selector(".ui-autocomplete-input").click()
        wd.find_element_by_css_selector(".ui-autocomplete-input").clear()
        wd.find_element_by_css_selector(".ui-autocomplete-input").send_keys(group_stations.to_station)
        time.sleep(1)
        wd.find_element_by_css_selector(".ui-autocomplete-input").send_keys(Keys.ENTER)
        wd.find_element_by_xpath("/html/body/div[2]/div[3]/form/div[3]/button").click()


    def choice_train(self):
        wd = self.wd
        time.sleep(1)
        wd.find_elements_by_css_selector("html body div#wrapper div#train-list.js-navigation-page.showed div.train-list.hide-no-place div.train-table div.item")[-1].click()
        time.sleep(1)


    def choice_types(self):
        wd = self.wd
        wd.find_elements_by_css_selector("html body div#wrapper div#train-wagons.js-navigation-page.showed div.types div.type")[-1].click()
        time.sleep(2)


    def choice_plase(self):
        wd = self.wd
        wd.find_element_by_css_selector(".inner-block").click()
        time.sleep(1)
        wd.find_element_by_css_selector("#wagons-popup > div:nth-child(1) > a:nth-child(2)").click()
        time.sleep(1)
        wd.find_element_by_xpath("/html/body/div[2]/div[6]/div/div[4]/div[2]/div/div/div[12]").click()
        time.sleep(1)
        wd.find_element_by_name("further").click()


    def doc_type_full(self, last_name, first_name):
        wd = self.wd
        wd.find_element_by_name("type").click()
        wd.find_element_by_name("type").find_element_by_css_selector("option:nth-child(1)").click()
        self.enter_name(last_name, first_name)
        time.sleep(1)
        wd.find_element_by_name("cart").click()


    def doc_type_child(self):
        pass

    def doc_type_student(self):
        pass

    def doc_type_beneficiary_beneficiary(self):
        pass

    def doc_type_beneficiary_accompanying(self):
        pass


    def enter_name(self, last_name, first_name):
        wd = self.wd
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(first_name)


    def pay(self, email_pay):
        wd = self.wd
        wd.find_element_by_css_selector(".ticket-pay > a:nth-child(2)").click()
        time.sleep(1)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email_pay)
        wd.find_element_by_name("is_confirmed").click()
        wd.find_element_by_css_selector(".button > button:nth-child(1)").click()
        time.sleep(3)


    def destroy(self):
        self.wd.quit()