# -*- coding: utf-8 -*-

from model.group_stations import Stations
from model.station_23_in_ukr_lang import station_list_23
import pytest
import random


testdata = [
    Stations(from_station=random.choice(station_list_23), to_station="Київ")
]


@pytest.mark.parametrize("stations", testdata, ids=[repr(x) for x in testdata])
def test_buy_ticket_outside_full(app, stations):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(stations)
    app.group.choice_train()
    app.group.choice_types()
#    app.group.choice_wagon()
    app.group.another_informations()
    app.group.doc_type_full(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")

def test_buy_ticket_outside_child(app, stations):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(stations)
    app.group.choice_train()
    app.group.choice_types()
#    app.group.choice_wagon()
    app.group.another_informations()
    app.group.doc_type_child(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")

def test_buy_ticket_outside_beneficiary(app, stations):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(stations)
    app.group.choice_train()
    app.group.choice_types()
#    app.group.choice_wagon()
    app.group.another_informations()
    app.group.doc_type_beneficiary(Num="Є047673", last_name="Сєдов", first_name="Микола")
    app.group.pay(email_pay="uz.all.test@gmail.com")

def test_buy_ticket_accompanying(app, stations):
    pass


def test_buy_ticket_transfers_full(app, stations):
    pass