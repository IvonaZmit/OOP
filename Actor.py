
class Actor(object):
    def __init__(self, name="", surname="", birth_year=0, films_list=""):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.films_list = films_list

    def __str__(self):
        return (f" Vardas: {self.name} Pavardė: {self.surname} Gimimo metai: {self.birth_year} Filmų sąrašas: {self.films_list}")