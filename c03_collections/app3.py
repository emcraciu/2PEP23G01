""""Create a self organising and self sorting phonebook - adding new users will keep dictionary order - removing users will preserve order"""
from collections import OrderedDict


class PhoneBook(object):
    phone_book = OrderedDict()

    def add_number(self, nume, numar):
        self.phone_book[nume] = numar
        sort_lst = self.phone_book.keys()
        sort_lst = sorted(sort_lst)
        for key in sort_lst:
            self.phone_book.move_to_end(key)

    def remove_number(self, nume):
        del self.phone_book[nume]

    def list_users(self):
        result = ""
        for name, number in self.phone_book.items():
            result += f"{name} : {number}\n"
        return result


book = PhoneBook()
book.add_number("Bob", 1224)
book.add_number("Carl", 1224)
book.add_number("Alice", 1224)
book.remove_number("Carl")
book.add_number("Denis", 1224)
book.add_number("Mihai", 1224)
print(book.phone_book)
print(book.list_users())
