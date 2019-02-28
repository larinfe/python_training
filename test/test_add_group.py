from model.group import Group

def test_add_group(app):
    app.group.create(Group("call", "cool", "cell"))
    app.session.logout()


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))
    app.session.logout()


