from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")
    #
    # def open_group_page(self):
    #     wd = self.wd
    #     wd.find_element_by_name("new").click()
    #
    # def submit_group_creation(self):
    #     wd = self.wd
    #     wd.find_element_by_name("submit").click()
    #
    # def fill_group_form(self, group):
    #     wd = self.wd
    #     self.open_group_page()
    #     wd.find_element_by_name("group_name").send_keys(group.name)
    #     wd.find_element_by_name("group_header").send_keys(group.header)
    #     wd.find_element_by_name("group_footer").send_keys(group.footer)
    #     wd.find_element_by_name("submit").click()
    #
    #
    #
    # def return_to_group_creation(self):
    #     wd = self.wd
    #     self.return_to_group_creation()
    #     wd.find_element_by_link_text("group page").click()



    def destroy(self):
        self.wd.quit()