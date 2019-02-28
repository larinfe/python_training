# -*- coding: utf-8 -*-
from model.contact import Contact



def test_modify_contact_firstname(app):
    app.group.modify_first_contact(Contact(firstname="AbraKadabra"))
    app.session.logout()

def test_modify_contact_middlename(app):
    app.group.modify_first_contact(Contact(middlename="Lossess"))
    app.session.logout()

