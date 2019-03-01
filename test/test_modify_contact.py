# -*- coding: utf-8 -*-
from model.contact import Contact



def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.fill_contact_form(Contact(address="test1"))
    app.contact.modify_first_contact(Contact(firstname="AbraKadabra1"))


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.fill_contact_form(Contact(firstname="test2"))
    app.contact.modify_first_contact(Contact(middlename="Lossess2"))


