class ContactList(list):

    def search(self, string):
        list = []
        for i in self:
            namelist = i.name.split()
            for name in namelist:
                if name == string:
                    list.append(i.name)
        return list

    def longest_name(self):
        name_list = []
        for i in self:
            name_list.append(i.name)
        if len(name_list) == 0:
            return None
        else:
            return max(name_list, key=len)


class Contact:

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        # cls.all_contacts = []
        cls.all_contacts.clear()


class Supplier(Contact):
    all_orders = {}

    def order(self, string):
        if self.email not in self.all_orders:
            self.all_orders.setdefault(self.email, [])
            self.all_orders[self.email].append(string)
        else:
            self.all_orders.setdefault(self.email, []).append(string)
