# -*- coding: utf-8 -*-


def test_del_contact(app):
    app.group.delete_first_contact()
