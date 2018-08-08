# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group_stations import Group
from fixture.group import GroupHelper


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_buy_ticket(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Group(from_station="Київ", to_station="Одеса"))
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_plase()
    app.group.doc_type_full(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")