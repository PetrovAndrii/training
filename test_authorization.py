# -*- coding: utf-8 -*-

import pytest
from application import Application




@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_authorization(app):
    app.open_mobile_page()
    app.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.logout()

def test_authorization_google(app):
    app.open_mobile_page()
    app.login_google(username="uz.all.test@gmail.com", password="P@ssw0rd!@#")
    app.logout()