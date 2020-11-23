from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, title=None, company=None, address=None, home_phone=None,
                 mobile_phone=None, work_phone=None, email=None, email2=None, email3=None, bday=0, bmonth="-",
                 byear=None, country=None, secondary_phone=None, notes=None, id=None, all_emails_from_home_page=None,
                 all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.country = country
        self.secondary_phone = secondary_phone
        self.notes = notes
        self.id = id
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
