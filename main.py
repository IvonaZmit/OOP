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

Hardy = Actor()
Hardy.name = "Tom"
Hardy.surname = "Hardy"
Hardy.birth_year = "1977"
print(Hardy.__str__())
Hardy = Actor("Tom", "Hardy", 1972)
print(Hardy.name, Hardy.surname, Hardy.birth_year)

DiCaprio = Actor()
DiCaprio.name = "Leonardo"
DiCaprio.surname = "DiCaprio"
DiCaprio.birth_year = "1974"
print(DiCaprio.__str__())
DiCaprio = Actor("Leonardo", "DiCaprio", 1974)
print(DiCaprio.name, DiCaprio.surname, DiCaprio.birth_year)

Jolie = Actor()
Jolie.name = "Angelina"
Jolie.surname = "Jolie"
Jolie.birth_year = "1975"
print(Jolie.__str__())
Jolie = Actor("Angelina", "Jolie", 1975)
print(Jolie.name, Jolie.surname, Jolie.birth_year)

print("----------------")

actors = []
actors.append(Hardy)
actors.append(DiCaprio)
actors.append(Jolie)

for actor in actors:
    print(actor.name, actor.surname, actor.birth_year)


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
