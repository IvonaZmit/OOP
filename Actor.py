
class Actor(object):
    def __init__(self, name="", surname="", birth_year=0):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def __str__(self):
        return (f" Vardas: {self.name} Pavardė: {self.surname} Gimimo metai: {self.birth_year}")