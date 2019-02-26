# -*- coding: utf-8 -*-
# import pytest
from model.contact import Contact
# from fixture.application_contact import Application_contact


# @pytest.fixture
# def app(request):
#     fixture = Application_contact()
#     request.addfinalizer(fixture.destroy)
#     return fixture

def test_del_contact(app):
    app.session_contact.login("admin", "secret")
    app.contact.delete_first_contact()
    app.session_contact.logout()