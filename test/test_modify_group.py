from model.group import Group

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="new group"))
    app.session.logout()

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="new group"))
    app.session.logout()