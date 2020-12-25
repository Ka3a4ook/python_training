from pytest_bdd import given, when, then
from model.contact import Contact
import random
import time


@given('a contact list', target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname> and <lastname>', target_fixture='new_contact')
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, new_contact, contact_list):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list', target_fixture='non_empty_contact_list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Andrey"))
    return db.get_contact_list()


@given('a random contact from the list', target_fixture='random_contact')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_added(db, random_contact, non_empty_contact_list, check_ui):
    old_contacts = non_empty_contact_list
    time.sleep(0.1)
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


@when('I modify the contact with <firstname> and <lastname>')
def modify_contact(app, random_contact, firstname, lastname):
    contact = Contact(firstname=firstname, lastname=lastname)
    app.contact.modify_contact_by_id(random_contact.id, contact)


@then('the new contact list is equal to the old list with the modified contact')
def verify_contact_modified(db, random_contact, non_empty_contact_list, check_ui, firstname, lastname):
    contact = Contact(firstname=firstname, lastname=lastname)
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    for index in range(len(old_contacts)):
        if old_contacts[index].id == random_contact.id:
            old_contacts[index].firstname = contact.firstname
            old_contacts[index].lastname = contact.lastname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
