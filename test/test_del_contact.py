# -*- coding: utf-8 -*-


def test_del_contact(app):
    app.session.login("admin", "secret")
    app.group.delete_all_contact()
    app.session.logout()