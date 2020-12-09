import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password,
                                                  autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, company, title, address, home, mobile, work, email, email2, email3,"
                "bday, bmonth, byear, address2, phone2, notes from addressbook")
            for row in cursor:
                (id, firstname, lastname, company, title, address, home, mobile, work, email, email2, email3, bday,
                 bmonth, byear, address2, phone2, notes) = row
                contact_list.append(
                    Contact(firstname=firstname, lastname=lastname, title=title, company=company, address=address,
                            home_phone=home, mobile_phone=mobile, work_phone=work, email=email, email2=email2,
                            email3=email3, bday=bday, bmonth=bmonth, byear=byear, country=address2,
                            secondary_phone=phone2, notes=notes, id=str(id)))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
