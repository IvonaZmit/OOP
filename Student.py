from datetime import date
from statistics import mean

class Student(object):
    def __init__(self, name="", surname="", birth_date=date, studies=dict):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.studies = studies

    def get_average_by_discipline(self, discipline= str):
        for object in self.studies.get("disciplines", []):
            if discipline in object:
                return round(mean(object[discipline]), 2)
        return None

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def __str__(self):
        return f"Vardas: {self.name}\n" f"Pavardė: {self.surname}\n" f"Gimimo metai: {self.birth_date}\n" f"Amžius: {self.get_age()}"
