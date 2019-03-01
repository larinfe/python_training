from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="list"))
    app.group.modify_first_group(Group(name="new grou2p"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="beas2t"))
    app.group.modify_first_group(Group(header="new group2"))
