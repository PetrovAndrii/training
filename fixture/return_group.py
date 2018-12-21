# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from model.group_stations import Stations
import time
from random import randint




class ReturnHelper:

    def __init__(self,app):
        self.app = app


    def choice_tiket_for_return(self):
        wd = self.app.wd
        links = wd.find_elements_by_css_selector(".return")
        l = links[randint(0, len(links) - 1)]
        l.click()
        if wd.find_elements_by_css_selector(".ok"):
            while wd.find_elements_by_css_selector(".ok"):
                wd.find_element_by_css_selector(".ok").click()
                self.app.group.open_actual_tikets()
                links = wd.find_elements_by_css_selector(".return")
                l = links[randint(0, len(links) - 1)]
                l.click()
        wd.find_elements_by_xpath("//*[contains(text(), 'Загальна сума повернення')]")


    def confirm_return(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".js-submit").click()
        elements = wd.find_elements_by_css_selector(".uid > b:nth-child(1)").copy()
        uid = "".join(element.text for element in elements)
        elements1 = wd.find_elements_by_css_selector("div.return-cost:nth-child(8) > b:nth-child(1)").copy()
        retu = "".join(element.text for element in elements1)
        elements2 = wd.find_elements_by_css_selector("div.return-cost:nth-child(8) > b:nth-child(3)").copy()
        cost = "".join(element.text for element in elements2)
        elements3 = wd.find_elements_by_css_selector("div.return-cost:nth-child(8) > b:nth-child(5)").copy()
        kept = "".join(element.text for element in elements3)
        print("")
        print("UID:", uid)
        print("Возврат:", retu)
        print("Стоимость:", cost)
        print("Удержано:", kept)


    def cancel_return(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".cancel").click()
