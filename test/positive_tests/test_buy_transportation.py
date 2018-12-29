# -*- coding: utf-8 -*-
import time
from model.group_stations import Stations


def test_buy_transt_cab(app):
    app.session.login(username="uz_test@yopmail.com", password="P@ssw0rd")
    app.group.open_actual_tikets()
    if not app.wd.find_elements_by_xpath("//*[contains(text(), 'У вас немає актуальних квитків')]"):
        pass
    else:
        app.group.search_train(Stations(from_station="Одеса", to_station="Київ"))
        app.group.choice_train()
        app.group.choice_types()
        app.group.choice_wagon()
        app.group.choice_plase()
        app.group.doc_type_full(last_name="test", first_name="uz")
        app.group.pay(email_pay="uz.all.test@gmail.com")
        app.group.open_actual_tikets()
    app.group.choice_trasportations()
    app.group.pay(email_pay="uz.all.test@gmail.com")
