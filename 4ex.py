import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts

    def save_to_file(self):
        with open(self.filename, "wb", encoding="utf-8") as f:
            pickle.dump(self, f)

    def read_from_file(self):
        with open(self.filename, 'rb', encoding="utf-8") as f:
            pickle.load(f)
