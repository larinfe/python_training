from model.contact import Contact


class ContactHelper:


    def __init__(self, app):
        self.app = app


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    # def select_first_group(self, wd):
    #     # select first group
    #     wd.find_element_by_name("selected[]").click()

    def submit_creation(self):
        # submit contact creation
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        # fill contact form
        wd = self.app.wd
        self.init_contact_creation()
        self.contact_field(contact)
        self.submit_creation()
        self.contact_cache = None

    def contact_field(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)

    def init_contact_creation(self):
        # init contact creation
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_app_page()
        # select first group
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_app_page()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a").click()
        # fill group form
        self.contact_field(new_contact_data)
        # submit
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_app_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_app_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")


    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_app_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=cells[1].text, firstname=cells[2].text, address=cells[3].text, id=id))

        return list(self.contact_cache)
