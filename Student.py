from datetime import date
from statistics import mean

class Student(object):
    def __init__(self, name= str, surname= str, birth_date= date, studies= dict):
        self.name = name.strip().capitalize()
        self.surname = surname.strip().capitalize()
        self.birth_date = birth_date
        self.studies = studies

    def add_grade(self, subject= str, grade= int):
        for object in self.studies["dalykas"]:
            if subject in object:
                object[subject].append(grade)
                return
        self.studies["dalykas"].append({subject:[grade]})

    def average(self, subject= str):
        for object in self.studies["dalykas"]:
            if subject in object:
                return round(mean(object[subject]), 2)
        return None


    def __str__(self):
        return f"Vardas: {self.name} Pavardė: {self.surname} Gimimo metai: {self.birth_date} Dalykas: {self.studies}"
