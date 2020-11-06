# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Andrey", lastname="Kazakevich", title="Engineer", company="Bercut",
                               home_phone="4226668", mobile_phone="89214226628",
                               email="89214226628@mail.ru", bday="4", bmonth="March", byear="1995",
                               country="Russia",
                               city="Saint-Petersburg",
                               notes="Hello everyone :)"))
    app.session.logout()