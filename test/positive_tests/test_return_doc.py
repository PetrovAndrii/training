# -*- coding: utf-8 -*-

from model.group_stations import Stations
import time
'''
Если билета нет, значить купить билет:
 1. полный
 2. рандомный
 3. льготный + сопровождающий:
    а) вернуть билет льготный - получить ошибку , что сначала нужно вернуть сопровождающего
    б) вернуть билет сопровождающий
    в) вернуть билет льготный
4. вернуть перевозочный
5. вернуть билет:
    - через актуальные билеты
    - через вкладку возврата (если ошибка "нужен фискальный номер",
                                          то переход на полную версию, взять данные с билета вернуть)
'''




def test_return_tiket(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.open_actual_tikets()
    if not app.wd.find_elements_by_xpath("//*[contains(text(), 'У вас немає актуальних квитків')]"):
        pass
    else:
        app.group.search_train(Stations(from_station="Вінниця", to_station="Харків"))
        app.group.choice_train()
        app.group.choice_types()
        app.group.choice_wagon()
        app.group.choice_plase()
        app.group.doc_type_full(last_name="test", first_name="uz")
        app.group.pay(email_pay="uz.all.test@gmail.com")
        app.group.open_actual_tikets()
    app.return_group.choice_tiket_for_return()
    app.return_group.confirm_return()


def test_cancel_return(app):
    app.session.login(username="uz.all.test@gmail.com", password="P@ssw0rd")
    app.group.open_actual_tikets()
    if not app.wd.find_elements_by_xpath("//*[contains(text(), 'У вас немає актуальних квитків')]"):
        pass
    else:
        app.group.search_train(Stations(from_station="Київ", to_station="Одеса"))
        app.group.choice_train()
        app.group.choice_types()
        app.group.choice_wagon()
        app.group.choice_plase()
        app.group.doc_type_full(last_name="test", first_name="uz")
        app.group.pay(email_pay="uz.all.test@gmail.com")
        app.group.open_actual_tikets()
    app.return_group.choice_tiket_for_return()
    app.return_group.cancel_return()


