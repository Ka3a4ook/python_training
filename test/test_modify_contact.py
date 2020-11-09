# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Andrey"))
    app.contact.modify_first_contact(Contact(firstname="Fedor", lastname="Emelyanenko"))
