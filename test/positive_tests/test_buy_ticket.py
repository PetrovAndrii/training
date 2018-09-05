# -*- coding: utf-8 -*-


from model.group_stations import Stations
import time

def test_buy_ticket_full(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station="Київ", to_station="Одеса"))
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_vagon()
    app.group.choice_plase()
    app.group.doc_type_full(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_child(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.search_train(Stations(from_station="Київ", to_station="Одеса"))
    app.group.choice_train()
    app.group.choice_types()
    app.group.choice_vagon()
    app.group.choice_plase()
    app.group.doc_type_child(last_name="test", first_name="uz")
    app.group.pay(email_pay="uz.all.test@gmail.com")


def test_buy_ticket_student(app):
    pass


def test_buy_ticket_beneficiary(app):
    pass


def test_buy_ticket_accompanying(app):
    pass


def test_buy_ticket_transfers(app):
    pass


def test_buy_ticket_outside(app):
    pass