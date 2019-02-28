# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    app.group.fill_contact_form(Contact("555qq23", "p1133p", "lo111l", "v1oron1ezh", "22222241222"))
    app.session.logout()

def test_add_contact_empty(app):
    app.group.fill_contact_form(Contact("", "", "", "", ""))
    app.session.logout()

