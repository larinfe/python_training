class ContactHelper:

    def __init__(self, app):
        self.app = app


    def submit_creation(self):
            # submit contact creation
            wd = self.app.wd
            wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
            # fill contact form
            wd = self.app.wd
            self.init_contact_creation()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
            wd.find_element_by_name("address").send_keys(contact.address)
            wd.find_element_by_name("home").send_keys(contact.home)
            self.submit_creation()

    def init_contact_creation(self):
            # init contact creation
            wd = self.app.wd
            wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
            wd = self.app.wd
            # select first group
            wd.get("http://localhost/addressbook/")
            wd.find_element_by_id("MassCB").click()
            wd.find_element_by_xpath("//input[@value='Delete']").click()
            # submit deletion
            wd.switch_to_alert().accept()
