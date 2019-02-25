# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_contact import Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.fill_contact_form(Contact("555555", "pup", "lol", "voronezh", "222222222"))
    app.logout()

def test_add_contact_empty(app):
    app.login( "admin", "secret")
    app.fill_contact_form(Contact("", "", "", "", ""))
    app.logout()

