# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Andrey"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    contact = Contact(firstname="Fedor", lastname="Emelyanenko")
    app.contact.modify_contact_by_id(random_contact.id, contact)
    new_contacts = db.get_contact_list()
    for index in range(len(old_contacts)):
        if old_contacts[index].id == random_contact.id:
            old_contacts[index].firstname = contact.firstname
            old_contacts[index].lastname = contact.lastname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
