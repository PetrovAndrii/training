# -*- coding: utf-8 -*-

from model.group_stations import Stations
from model.station_22_in_ukr_lang import station_list_22
import pytest
import random


testdata = [
    Stations(from_station=random.choice(station_list_22), to_station=random.choice(station_list_22))
]


@pytest.mark.parametrize("stations", testdata, ids=[repr(x) for x in testdata])
def test_buy_ticket_full(app, stations):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(stations)
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.choice_plase()
    app.group.doc_type_full(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_child(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station="Київ", to_station="Одеса"))
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.choice_plase()
    app.group.doc_type_child(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_student(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station="Київ", to_station="Одеса"))
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.choice_plase()
    app.group.doc_type_student(STUD="ХА11072388", last_name="Коломійцева", first_name="Тетяна")
    if app.wd.find_elements_by_css_selector(".popup-canvas"):
        app.wd.find_element_by_css_selector(".ok").click()
        app.group.search_train(Stations(from_station="Київ", to_station="Одеса"))
        app.group.choice_train()
        app.group.choice_types()
        app.group.choice_wagon()
        app.group.choice_plase()
        app.group.doc_type_student(STUD="ХА11072388", last_name="Коломійцева", first_name="Тетяна")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_beneficiary(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station="Київ", to_station="Одеса"))
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.choice_plase()
    app.group.doc_type_beneficiary(Num="В-І322262", last_name="Колісник", first_name="Наталія")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_accompanying(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station="Київ", to_station="Одеса"))
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.choice_plase()
    app.group.doc_type_beneficiary(Num="В-І322262", last_name="Колісник", first_name="Наталія")
    app.group.doc_type_accompanying(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_transfers_full(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station="Київ", to_station="Одеса"))
    app.group.search_transfer()
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.choice_plase()
    app.group.doc_type_full(last_name="test", first_name="uz")
    app.group.choice_types()
    app.group.choice_wagon()
    app.group.choice_plase()
    app.group.doc_type_full(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")
