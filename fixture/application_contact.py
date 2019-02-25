from selenium import webdriver
from fixture.session_contact import SessionHelper_contact

class Application_contact:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_contact = SessionHelper_contact(self)

    # def logout(self):
    #     # logout
    #     wd = self.wd
    #     wd.find_element_by_link_text("Logout").click()

    def submit_creation(self):
        # submit contact creation
        wd = self.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        # fill contact form
        wd = self.wd
        self.init_contact_creation()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)
        self.submit_creation()

    def init_contact_creation(self):
        # init contact creation
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    # def login(self, username, password):
    #     # login
    #     wd = self.wd
    #     self.open_home_page()
    #     wd.find_element_by_name("user").send_keys(username)
    #     wd.find_element_by_name("pass").send_keys(password)
    #     wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self,):
        # open home page
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()

