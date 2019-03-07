# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_contact_form(Contact(firstname="test1"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) -1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts