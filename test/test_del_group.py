


def test_delete__first_group(app):
    app.group.delete_first_group()
    app.session.logout()