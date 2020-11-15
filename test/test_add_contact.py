# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Andrey", lastname="Kazakevich", title="Engineer", company="Bercut",
                               home_phone="4226668", mobile_phone="89214226628",
                               email="89214226628@mail.ru", bday="4", bmonth="March", byear="1995",
                               country="Russia",
                               city="Saint-Petersburg",
                               notes="Hello everyone :)"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
