# -*- coding: utf-8 -*-
import pytest
from fixture.application_contact import Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture
