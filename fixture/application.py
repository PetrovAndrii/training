from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.return_group import ReturnHelper
from fixture.regist_group import RegistrationHelper



class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.return_group = ReturnHelper(self)
        self.regist_group = RegistrationHelper(self)
        self.base_url = base_url


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_mobile_page(self):
        wd = self.wd
        wd.get(self.base_url)
        if (wd.find_elements_by_css_selector(".mobile-version")):
            wd.find_element_by_css_selector(".mobile-version").click()
            wd.execute_script("document.cookie='_uz_emu_on=__on__; path=/; expires=Sun, 01-Jan-2045 00:00:00 GMT'")



    def destroy(self):
        self.wd.quit()