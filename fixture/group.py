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
        self.open_group_page()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
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