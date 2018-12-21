# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from model.group_stations import Stations
import time
from random import randint




class GroupHelper:

    def __init__(self,app):
        self.app = app


    def search_train(self, group_stations):
        wd = self.app.wd
        wd.find_element_by_css_selector(".logo").click()
        wd.find_element_by_name("from-title").click()
        wd.find_element_by_css_selector(".ui-autocomplete-input").click()
        wd.find_element_by_css_selector(".ui-autocomplete-input").clear()
        wd.find_element_by_css_selector(".ui-autocomplete-input").send_keys(group_stations.from_station)
        time.sleep(1)
        wd.find_element_by_css_selector(".ui-autocomplete-input").send_keys(Keys.ENTER)
        wd.find_element_by_name("to-title").click()
        wd.find_element_by_css_selector(".ui-autocomplete-input").click()
        wd.find_element_by_css_selector(".ui-autocomplete-input").clear()
        wd.find_element_by_css_selector(".ui-autocomplete-input").send_keys(group_stations.to_station)
        time.sleep(1)
        wd.find_element_by_css_selector(".ui-autocomplete-input").send_keys(Keys.ENTER)
        wd.find_element_by_xpath("/html/body/div[2]/div[3]/form/div[3]/button").click()
        if wd.find_elements_by_css_selector(".search-error"):
            while wd.find_elements_by_css_selector(".search-error"):
                self.search_train(Stations(from_station="Київ", to_station="Одеса"))


    def search_transfer(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@type='button']").click()
        time.sleep(5)


    def choice_train(self):
        wd = self.app.wd
        time.sleep(1)
        links = [link for link in wd.find_elements_by_class_name("item") if link.is_displayed()]
        l = links[randint(0, len(links)-1)]
        l.click()
        time.sleep(1)


    def choice_types(self):
        wd = self.app.wd
        time.sleep(1)
        links = [link for link in wd.find_elements_by_class_name("type") if link.is_displayed()]
        l = links[randint(0, len(links) - 1)]
        l.click()
        time.sleep(2)


    def choice_wagon(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".inner-block").click()
        links = wd.find_elements_by_xpath("/html/body/div[5]/div/a")
        l = links[randint(0, len(links)-1)]
        l.click()
        time.sleep(1)


    def another_informations(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".plus").click()
        wd.find_element_by_name("further").click()


    def choice_plase(self):
        wd = self.app.wd
        links = wd.find_elements_by_xpath("//div[@original-place]")
        l = links[randint(0, len(links)-1)]
        l.click()
        time.sleep(1)
        wd.find_element_by_name("further").click()


    def add_cart(self):
        wd = self.app.wd
        if (wd.find_elements_by_name("cart")):
            wd.find_element_by_name("cart").click()
        if (wd.find_elements_by_css_selector(".next-button > button:nth-child(1)")):
            wd.find_element_by_css_selector(".next-button > button:nth-child(1)").click()
        if wd.find_elements_by_css_selector(".ok"):
            wd.find_element_by_css_selector(".ok").click()

    def doc_type_full(self, last_name, first_name):
        wd = self.app.wd
        wd.find_element_by_name("type").click()
        wd.find_element_by_name("type").find_element_by_css_selector("option:nth-child(1)").click()
        self.enter_name(last_name, first_name)
        time.sleep(1)
        self.add_cart()


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
        self.add_cart()


    def doc_type_student(self, STUD, last_name, first_name):
        wd = self.app.wd
        wd.find_element_by_name("type").click()
        wd.find_element_by_name("type").find_element_by_css_selector("option:nth-child(3)").click()
        wd.find_element_by_name("student").click()
        wd.find_element_by_name("student").clear()
        wd.find_element_by_name("student").send_keys(STUD)
        self.enter_name(last_name, first_name)
        self.add_cart()


    def doc_type_beneficiary(self, Num, last_name, first_name):
# какого то хрена поиск по имени, нормальному селектору или хпасу падает, потому что не скролится
        wd = self.app.wd
        wd.find_element_by_name("type").click()
        wd.find_element_by_name("type").find_element_by_css_selector("option:nth-child(4)").click()
        wd.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div[1]/div[2]/input").click()
        wd.find_element_by_css_selector("label.item:nth-child(4) > div:nth-child(2)").click()
        time.sleep(1)
        wd.find_element_by_css_selector("div.type-box:nth-child(2) > div:nth-child(2) > input:nth-child(2)").send_keys(Num)
        wd.find_element_by_css_selector("div.button:nth-child(4) > button:nth-child(1)").click()
        self.enter_name(last_name, first_name)
        self.add_cart()


    def doc_type_beneficiary_out(self, Num, last_name, first_name):
        # какого то хрена поиск по имени, нормальному селектору или хпасу падает, потому что не скролится
        wd = self.app.wd
        wd.find_element_by_name("type").click()
        wd.find_element_by_name("type").find_element_by_css_selector("option:nth-child(3)").click()
        wd.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div[1]/div[2]/input").click()
        wd.find_element_by_css_selector("label.item:nth-child(4) > div:nth-child(2)").click()
        time.sleep(1)
        wd.find_element_by_css_selector("div.type-box:nth-child(2) > div:nth-child(2) > input:nth-child(2)").send_keys(Num)
        wd.find_element_by_css_selector("div.button:nth-child(4) > button:nth-child(1)").click()
        self.enter_name(last_name, first_name)
        self.add_cart()



    def doc_type_accompanying(self, last_name, first_name):
        wd = self.app.wd
        time.sleep(3)
        wd.find_element_by_css_selector(".buy-convoy").click()
        self.choice_types()
        self.choice_plase()
        time.sleep(3)
        self.enter_name(last_name, first_name)
        self.add_cart()


    def doc_type_accompanying_out(self, last_name, first_name):
        wd = self.app.wd
        time.sleep(3)
        wd.find_element_by_css_selector(".buy-convoy").click()
        self.choice_types()
        self.another_informations()
        time.sleep(3)
        self.enter_name(last_name, first_name)
        self.add_cart()


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


    def enter_card(self):
        wd = self.app.wd
        time.sleep(1)
        wd.find_element_by_name("cnum").click()
        wd.find_element_by_name("cnum").send_keys("4911")
        wd.find_element_by_name("cnum").click()
        wd.find_element_by_name("cnum").send_keys("9900")
        wd.find_element_by_name("cnum").click()
        wd.find_element_by_name("cnum").send_keys("9999")
        wd.find_element_by_name("cnum").click()
        wd.find_element_by_name("cnum").send_keys("9999")
        wd.find_element_by_name("expire_month").click()
        wd.find_element_by_name("expire_month").clear()
        wd.find_element_by_name("expire_month").send_keys("12")
        wd.find_element_by_name("expire_year").click()
        wd.find_element_by_name("expire_year").clear()
        wd.find_element_by_name("expire_year").send_keys("19")
        wd.find_element_by_name("cvv[new]").click()
        wd.find_element_by_name("cvv[new]").clear()
        wd.find_element_by_name("cvv[new]").send_keys("123")
        wd.find_element_by_xpath('//*[@id="service_confirm_payment_button"]').click()
        time.sleep(5)


    def open_menu(self):
        wd = self.app.wd
        self.app.open_mobile_page()
        wd.find_element_by_class_name("ic-menu").click()


    def open_cabinet(self):
        wd = self.app.wd
        self.open_menu()
        wd.find_element_by_css_selector(".slide-menu > a:nth-child(3)").click()


    def open_actual_tikets(self):
        wd = self.app.wd
        self.open_cabinet()
        wd.find_element_by_css_selector("#cabinet-menu > a:nth-child(1)").click()


