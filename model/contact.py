from sys import maxsize


class Contact:

    def __init__(self, firstname = None, middlename=None, lastname=None, address=None, home=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.home = home
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (str(self.id), self.lastname, self.firstname, self.address, self.home)

    def __eq__(self, other):
        # return self.id == other.id and self.lastname == other.lastname
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname\
               and self.firstname == other.firstname and self.address == other.address


    def id_or_max(cn):
        if cn.id:
            return int(cn.id)
        else:
            return maxsize