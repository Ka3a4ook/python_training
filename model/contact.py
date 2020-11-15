from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, title=None, company=None, home_phone=None, mobile_phone=None,
                 email=None, bday=0, bmonth="-", byear=None,
                 country=None, city=None, notes=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.company = company
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.country = country
        self.city = city
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % self.id

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
