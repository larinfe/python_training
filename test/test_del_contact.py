# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_contact_form(Contact(firstname="test1"))
    app.contact.delete_first_contact()
