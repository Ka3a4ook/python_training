from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # main information
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        # telephone
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        # email
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        # birthday
        if contact.bday != 0:
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        if contact.bmonth != '-':
            # wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
            # wd.find_element_by_xpath("//option[@value='%s']" % contact.bmonth).click()
        self.change_field_value("byear", contact.byear)
        # address
        self.change_field_value("address2", contact.country)
        self.change_field_value("phone2", contact.secondary_phone)
        # notes
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # select contact
        self.select_contact_by_id(id)
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = text[2].text
                lastname = text[1].text
                address = text[3].text
                all_emails = text[4].text
                all_phones = text[5].text
                self.contact_cache.append(
                    Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                            all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2,
                       email3=email3, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       secondary_phone=secondary_phone)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(id=id, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       secondary_phone=secondary_phone)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % contact.id).click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group.name)
        wd.find_element_by_name("add").click()
        self.return_to_home_page()

    def delete_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.return_to_home_page()
        Select(wd.find_element_by_name("group")).select_by_visible_text(group.name)
        wd.find_element_by_css_selector("input[value='%s']" % contact.id).click()
        wd.find_element_by_name("remove").click()
        self.return_to_home_page()
