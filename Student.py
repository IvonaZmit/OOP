from datetime import date
from statistics import mean

class Student(object):
    def __init__(self, name="", surname="", birth_date=date, studies=dict):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.studies = studies

    def add_grade(self, subject= str, grade= int):
        for object in self.studies["disciplines"]:
            if subject in object:
                object[subject].append(grade)
                return
        self.studies["disciplines"].append({subject:[grade]})

    def average(self, subject= str):
        for object in self.studies["disciplines"]:
            if subject in object:
                return round(mean(object[subject]), 2)
        return None


    def __str__(self):
        return f"Vardas: {self.name}, Pavardė: {self.surname}, Gimimo metai: {self.birth_date}, Disciplina: {self.studies}."
