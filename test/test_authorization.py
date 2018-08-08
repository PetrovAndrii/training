# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_authorization(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.session.logout()


def test_authorization_google(app):
    app.session.login_google(username="uz.all.test@gmail.com", password="P@ssw0rd!@#")
    app.session.logout()
