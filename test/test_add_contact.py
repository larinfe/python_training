# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.fill_contact_form(Contact(firstname="555qq23", middlename="p1133p", lastname="lo111l", address="v1oron1ezh", home="22222241222"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

def test_add_contact_empty(app):
    app.contact.fill_contact_form(Contact(firstname="", middlename="", lastname="", address="", home=""))


