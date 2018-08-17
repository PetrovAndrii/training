# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
import time
from random import randint




class GroupHelper:

    def __init__(self,app):
        self.app = app


    def search_train(self, group_stations):
        wd = self.app.wd
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
        wd = self.app.wd
        time.sleep(1)
        links = [link for link in wd.find_elements_by_class_name("item") if link.is_displayed()]
        l = links[randint(0, len(links)-1)]
        l.click()
        time.sleep(1)


    def choice_types(self):
        wd = self.app.wd
        links = [link for link in wd.find_elements_by_class_name("type") if link.is_displayed()]
        l = links[randint(0, len(links)-1)]
        l.click()
        time.sleep(2)


    def choice_plase(self):
        wd = self.app.wd
        links = wd.find_elements_by_xpath("//div[@original-place]")
        l = links[randint(0, len(links)-1)]
        l.click()
        time.sleep(1)
        wd.find_element_by_name("further").click()


    def doc_type_full(self, last_name, first_name):
        wd = self.app.wd
        wd.find_element_by_name("type").click()
        wd.find_element_by_name("type").find_element_by_css_selector("option:nth-child(1)").click()
        self.enter_name(last_name, first_name)
        time.sleep(1)
        wd.find_element_by_name("cart").click()


    def doc_type_child(self, last_name, first_name):
        wd = self.app.wd
        wd.find_element_by_name("type").click()
        wd.find_element_by_name("type").find_element_by_css_selector("option:nth-child(2)").click()
        wd.find_element_by_name("child-hover").click()
        wd.find_element_by_css_selector(".ui-calendar-year-list-table > a:nth-child(10)").click()
        wd.find_element_by_css_selector(".ui-calendar-month-list-table > a:nth-child(1)").click()
        wd.find_element_by_xpath("/html/body/div[4]/div/div/table/tbody/tr[2]/td[3]/a").click()
        self.enter_name(last_name, first_name)
        time.sleep(1)
        wd.find_element_by_name("cart").click()


    def doc_type_student(self):
        pass


    def doc_type_beneficiary_beneficiary(self):
        pass


    def doc_type_beneficiary_accompanying(self):
        pass


    def enter_name(self, last_name, first_name):
        wd = self.app.wd
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(first_name)


    def pay(self, email_pay):
        wd = self.app.wd
        wd.find_element_by_css_selector(".ticket-pay > a:nth-child(2)").click()
        time.sleep(1)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email_pay)
        wd.find_element_by_name("is_confirmed").click()
        wd.find_element_by_css_selector(".button > button:nth-child(1)").click()
        time.sleep(3)