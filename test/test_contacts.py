import re
from random import randrange
from model.contact import Contact


# def test_contact_on_home_and_edit_page(app):
#     index = randrange(len(app.contact.get_contact_list()))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert (contact_from_home_page.firstname, contact_from_home_page.lastname, contact_from_home_page.address,
#             contact_from_home_page.all_emails_from_home_page, contact_from_home_page.all_phones_from_home_page) == \
#            (contact_from_edit_page.firstname, contact_from_edit_page.lastname, contact_from_edit_page.address,
#             merge_emails_like_on_home_page(contact_from_edit_page),
#             merge_phones_like_on_home_page(contact_from_edit_page))


# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
#     assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
#     assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
#     assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone

def test_contact_on_home_page_and_db(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = db.get_contact_list()
    for index in range(len(contact_from_home_page)):
        assert (contact_from_home_page[index].firstname, contact_from_home_page[index].lastname,
                contact_from_home_page[index].address, contact_from_home_page[index].all_emails_from_home_page,
                contact_from_home_page[index].all_phones_from_home_page) == \
               (contact_from_db[index].firstname, contact_from_db[index].lastname, contact_from_db[index].address,
                merge_emails_like_on_home_page(contact_from_db[index]),
                merge_phones_like_on_home_page(contact_from_db[index]))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                          [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                                           contact.secondary_phone]))))
