# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Andrey", lastname="Kazakevich", title="Engineer", company="Bercut",
                      address="Russia, SPb, Vasilyevskiy island", home_phone="4226668", mobile_phone="8-921-422-66-28",
                      work_phone="123-456-789", email="89214226628@mail.ru", email2="abrakadabra@mail.ru",
                      email3="vasya.pupkin@mail.ru", bday="4", bmonth="March", byear="1995", country="Russia",
                      secondary_phone="(123)456-78-45", notes="Hello everyone :)")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
