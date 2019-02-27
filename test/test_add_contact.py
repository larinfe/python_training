# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    app.session.login("admin", "secret")
    app.group.fill_contact_form(Contact("555555", "pup", "lol", "voronezh", "222222222"))
    app.session.logout()

def test_add_contact_empty(app):
    app.session.login( "admin", "secret")
    app.group.fill_contact_form(Contact("", "", "", "", ""))
    app.session.logout()

