# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
import time
from random import randint




class RegistrationHelper:

    def __init__(self,app):
        self.app = app


    def new_account(self):
        wd = self.app.wd
        self.app.open_mobile_page()

        pass
