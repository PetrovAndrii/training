# -*- coding: utf-8 -*-

from model.group_stations import Stations
from model.station_23_in_ukr_lang import station_list_23
import pytest
import random
import time


testdata = [
    Stations(from_station=random.choice(station_list_23), to_station="Київ")
]


@pytest.mark.parametrize("stations", testdata, ids=[repr(x) for x in testdata])
def test_buy_ticket_outside_full(app, stations):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(stations)
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.another_informations()
    app.group.doc_type_full(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_outside_child(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station=random.choice(station_list_23), to_station="Київ"))
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.another_informations()
    app.group.doc_type_child(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_outside_beneficiary(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station=random.choice(station_list_23), to_station="Київ"))
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.another_informations()
    app.group.doc_type_beneficiary_out(Num="В-І322262", last_name="Колісник", first_name="Наталія")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_accompanying(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station=random.choice(station_list_23), to_station="Київ"))
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.another_informations()
    app.group.doc_type_beneficiary_out(Num="В-І322262", last_name="Колісник", first_name="Наталія")
    app.group.doc_type_accompanying_out(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_transfers_full(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station="Москва Київська", to_station="Ніжин"))
    app.group.search_transfer()
    time.sleep(10)
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.another_informations()
    app.group.doc_type_full(last_name="test", first_name="uz")
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.choice_plase()
    app.group.doc_type_full(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")