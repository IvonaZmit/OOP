#Sukurti klasę Actor.
#Properties:
#name
#surname
#birth_year
#(extra, films list)
#naudojame __str___ atspausdinimui

#sukurti 3 objektus su reikšmėmis naudojantis tuščiu konstruktoriu, ir tris naudojantis pilnu konstuktoriu.
#sudėti juos į aktorių masyvą.
#prasukti ciklą per masyvą ir atspausdinti aktorius (jei aktoriai turi filmus atspausti ir juos)


from Actor import Actor
from Plant import Plant
from Student import Student
from datetime import date
from statistics import mean

Hardy = Actor()
Hardy.name = "Tom"
Hardy.surname = "Hardy"
Hardy.birth_year = "1977"
Hardy.films_list = "Venom, Venom 2, Havoc"
print(Hardy.__str__())
Hardy = Actor("Tom", "Hardy", 1977, "Venom, Venom 2, Havoc")
print(Hardy.name, Hardy.surname, Hardy.birth_year, Hardy.films_list)

DiCaprio = Actor()
DiCaprio.name = "Leonardo"
DiCaprio.surname = "DiCaprio"
DiCaprio.birth_year = "1974"
DiCaprio.films_list = "Titanic, Inception, Billy"
print(DiCaprio.__str__())
DiCaprio = Actor("Leonardo", "DiCaprio", 1974, "Titanic, Inception, Billy")
print(DiCaprio.name, DiCaprio.surname, DiCaprio.birth_year, DiCaprio.films_list)

Jolie = Actor()
Jolie.name = "Angelina"
Jolie.surname = "Jolie"
Jolie.birth_year = "1975"
Jolie.films_list = "Salt, Wanted, Mr.&Mrs. Smith"
print(Jolie.__str__())
Jolie = Actor("Angelina", "Jolie", 1975, "Salt, Wanted, Mr.&Mrs. Smith")
print(Jolie.name, Jolie.surname, Jolie.birth_year, Jolie.films_list)

print("----------------")

actors = []
actors.append(Hardy)
actors.append(DiCaprio)
actors.append(Jolie)

for actor in actors:
    print(actor.name, actor.surname, actor.birth_year, actor.films_list)


print("------------------")
#Sukurti klasę Plant
#Klasės laukai:
#Pavadinimas
#lotyniskas pavadinimas
#boolean vienmetis
#kokiam zemyne auga
#suaugusio augalo aukstis metrais.
#ar valgomas?
#naudojame __str___ atspausdinimui (atvaizdavimui praverčia ternary operator)
#Susikuriam masyvą saugoti augalams. sukuriame 4 augalus (2x2 pagal konstruktorius)
#prasukti ciklą ir atspausdinti augalus

Sunflower = Plant()
Sunflower.name = "Sunflower"
Sunflower.latin_name = "Helianthus annuus"
Sunflower.annual = True
Sunflower.continent = "North America"
Sunflower.adult_height = "1.5-3m"
Sunflower.edible = True
print(Sunflower.__str__())


Lavender = Plant()
Lavender.name = "Lavender"
Lavender.latin_name = "Lavandula angustifolia"
Lavender.annual = False
Lavender.continent = "Europe"
Lavender.adult_height = "0.5-1m"
Lavender.edible = True
print(Lavender.__str__())

Corn = Plant("Corn", "Zea mays", True, "North & South America", "2-3m", True)
print(Corn.name, Corn.latin_name, Corn.annual, Corn.continent, Corn.adult_height, Corn.edible)


Rosemary = Plant("Rosemary", "Salvia rosmarinus", False, "Europe", "1-2m", True)
print(Rosemary.name, Rosemary.latin_name, Rosemary.annual, Rosemary.continent, Rosemary.adult_height, Rosemary.edible)


print("----------------")

plants = []
plants.append(Sunflower)
plants.append(Lavender)
plants.append(Corn)
plants.append(Rosemary)

for plant in plants:
    print(plant.name, plant.latin_name, plant.annual, plant.continent, plant.adult_height, plant.edible)

print("-----------------------")
#Sukurti klasę Student
#vardas (suformatuojame iki teisingo užrašymo)
#pavardė (suformatuojame iki teisingo užrašymo)
#gimimo data date
#studies dictionary{
#           "disciplines:[
#               {"matematika": [8,7,9]},
#               { "geografija": [7,5,6,10,8,9,9]}
#            ]
#sukurti metodą get_age() kuris gražintų tikslų, gražiai suformatuotą amžių su metais, mėnesiais ir dienomis
#sukurti metodą, kuris padavus disciplinos pavadinimą gražintų jos pažymių vidurkį
#sukurti metodą, kuris paskaičiuotų visų disciplinų(int) vidurkių vidurkį(double). galima kurtis pagalbines funkcijas.
#parašyti __str__ kuris gražiai atspausdintų visą išsamią, gražiai suformatuotą studento informaciją


Jonas = Student()
Jonas.name = "Jonas"
Jonas.surname = "Petraitis"
Jonas.birth_date = date(1985, 8, 20)
Jonas.studies = {
    "disciplines": [
        {"matematika": [8, 7, 9]},
        {"geografija": [7, 5, 6, 10, 8, 9, 9]}
    ]
}

print("Matematikos vidurkis:", Jonas.get_average_by_discipline("matematika"))
print("Geografijos vidurkis:", Jonas.get_average_by_discipline("geografija"))

print(Jonas)



