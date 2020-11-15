# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Andrey"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="Fedor", lastname="Emelyanenko"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
