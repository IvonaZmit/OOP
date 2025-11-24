
class Plant(object):
    def __init__(self, name="", latin_name="", annual=True, continent="", adult_height="", edible=True ):
        self.name = name
        self.latin_name = latin_name
        self.annual = annual
        self.continent = continent
        self.adult_height = adult_height
        self.edible = edible

    def __str__(self):
        return (f'Augalo pavadinimas: {self.name}, lotyniskas pavadinimas: {self.latin_name}, vienmetis:'
                f'{"Taip" if self.annual else "Ne"}, '
                f'Kokiam zemyne auga: {self.continent}, suaugusio augalo aukstis: {self.adult_height}, ar valgomas:'
                f'{"Taip" if self.edible else "Ne"}')



