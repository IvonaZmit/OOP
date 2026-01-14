from datetime import date
from statistics import mean

class Student(object):
    def __init__(self, name="", surname="", birth_date=None, studies=None):
        self.name = name.strip().capitalize()
        self.surname = surname.strip().capitalize()
        self.birth_date = birth_date
        self.studies = studies if studies else {"disciplines": []}

    def get_average_by_discipline(self, discipline= str) -> float | None:
        for object in self.studies.get("disciplines", []):
            if discipline in object:
                return round(mean(object[discipline]), 2)
        return None

    def get_overall_average_by_discipline(self) -> float | None:
        averages = []

        for object in self.studies.get("disciplines", []):
            for grades in object.values():
                if grades:
                    averages.append(mean(grades))

        if not averages:
            return None

        return round(mean(averages), 2)

    def get_age(self) -> int | None:
        if not self.birth_date:
            return None

        today = date.today()
        age = today.year - self.birth_date.year

        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1

        return age

    def __str__(self):
        return (
            f"Vardas: {self.name}\n" 
            f"Pavardė: {self.surname}\n" 
            f"Gimimo metai: {self.birth_date}\n" 
            f"Amžius: {self.get_age()}\n" 
            f"Bendras vidurkis: {self.get_overall_average_by_discipline()}"
        )