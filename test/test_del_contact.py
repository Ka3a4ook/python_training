# -*- coding: utf-8 -*-
from model.contact import Contact
import time
from random import randrange


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Andrey"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    time.sleep(0.1)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
