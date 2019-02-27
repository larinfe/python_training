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
        # fill group  from
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def return_to_group_creation(self):
        wd = self.app.wd
        self.return_to_group_creation()
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.open_home_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("group page").click()

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

    def delete_all_contact(self):
            wd = self.app.wd
            # select first group
            wd.get("http://localhost/addressbook/")
            wd.find_element_by_id("MassCB").click()
            wd.find_element_by_xpath("//input[@value='Delete']").click()
            # submit deletion
            wd.switch_to_alert().accept()