# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group_stations import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_buy_ticket(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.search_train(Group(from_station="Київ", to_station="Одеса"))
    app.choice_train()
    app.choice_types()
    app.choice_plase()
    app.doc_type_full(last_name="test", first_name="uz")
    app.pay(email_pay="uz.all.test@gmail.com")