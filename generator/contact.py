from model.contact import Contact
import random
import string
import re
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join(map(lambda x: clear(x), [random.choice(symbols) for i in range(random.randrange(maxlen))]))


def random_email(postfix, maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix


def random_number(prefix):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randint(7, 8))])


def random_bday():
    return str(random.randint(1, 31))


bmonth_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']


def random_bmonth():
    return random.choice(bmonth_list)


def random_byear(prefix):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(2, 3))])


def clear(s):
    return re.sub(r"[\\'<>]", "", s)


testdata = [Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20),
                    title=random_string("title", 20), company=random_string("company", 20),
                    address=random_string("address", 20), home_phone=random_number("+7812"),
                    mobile_phone=random_number("+7-921-"), work_phone=random_number(""),
                    email=random_email("@mail.ru", 10), email2=random_email("@yandex.ru", 15),
                    email3=random_email("@gmail.com", 20), bday=random_bday(), bmonth=random_bmonth(),
                    byear=random_byear("19"), country=random_string("country", 20),
                    secondary_phone=random_number("+7(921)"), notes=random_string("notes", 20)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
