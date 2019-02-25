# -*- coding: utf-8 -*-
from selenium import webdriver
from contact import Contact
import unittest

class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.init_contact_creation(wd)
        self.fill_contact_form(wd, Contact("555555","pup","lol","voronezh","222222222"))
        self.submit_creation(wd)
        self.logout(wd)

    def test_add_contact_empty(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.init_contact_creation(wd)
        self.fill_contact_form(wd, Contact("", "", "", "", ""))
        self.submit_creation(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def submit_creation(self, wd):
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, wd, contact):
        # fill contact form
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)

    def init_contact_creation(self, wd):
        # init contact creation
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()



if __name__ == "__main__":
    unittest.main()
