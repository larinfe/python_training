

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.fill_group_form(Group(name="call", header="cool", footer="cell"))
    app.logout()


def test_add_empty_group(app):
    app.login(username = "admin", password = "secret")
    app.fill_group_form(Group(name = "", header = "", footer = ""))
    app.logout()


