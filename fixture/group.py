class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # init group creation
        self.open_group_page()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def return_to_group_creation(self):
        wd = self.app.wd
        self.return_to_group_creation()
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.open_home_page()
        self.select_first_group(wd)
        # submit deletion
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("group page").click()

    def select_first_group(self, wd):
        # select first group
        wd.find_element_by_name("selected[]").click()

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

    def delete_all_contact(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        # select first group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group(wd)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form

        self.fill_group_form(new_group_data)
        # submit
        wd.find_element_by_name("update").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("selected[]").click()
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a").click()
        # fill group form
        self.contact_field(new_contact_data)
        # submit
        wd.find_element_by_name("update").click()