class Contact:

    def __init__(self, firstname=None, lastname=None, title=None, company=None, home_phone=None, mobile_phone=None,
                 email=None, bday=0, bmonth="-", byear=None,
                 country=None, city=None, notes=None):
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
