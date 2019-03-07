# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange



def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_contact_form(Contact(address="test1"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(address="AbraKadabra1")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # assert old_contacts == new_contacts




# def test_modify_contact_middlename(app):
#     if app.contact.count() == 0:
#         app.contact.fill_contact_form(Contact(firstname="test2"))
#     app.contact.modify_first_contact(Contact(middlename="Lossess2"))


