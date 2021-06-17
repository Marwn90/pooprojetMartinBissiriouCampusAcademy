

# Création de la classe
from Parent import Parent

"""
class People:
    def __init__(self, name, height, mass, hair_color, skin_color, eye_color, birth_year, gender, homeworld, films, species, vehicles, starships, created, edited, url):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.films = films
        self.species = species
        self.vehicles = vehicles
        self.starships = starships
        self.created = created
        self.edited = edited
        self.url = url
        """


class People(Parent):
    def __init__(self, name, height, mass, hair_color, skin_color, eye_color, birth_year, gender, homeworld, films, species, vehicles, starships, created, edited, url):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.films = films
        self.species = species
        self.vehicles = vehicles
        self.starships = starships



# Definition des methodes

def mange(self, message):
    print("{}  a manger : {}".format(self.name, message))
    return message






# Création de l'objet avec people 
# Creation du premier objet people1
personne1 =  People ("Jack", "1m77", "90 kg", "black", "yellow", "blue", "1797", "Male", "Earth", "Rambo", "phelin", "Range Rover", "fusé", "1988", "1900","https://www.linguee.fr/anglais-francais/traduction/height.html")

# Creation du second  objet people2

personne2 = People("Manon", "1m73", "98 kg", "White", "yellow", "blue", "1997", "female", "Earth", "Terminator", "phelin", "Rolls royce", "fusé", "1942", "1943","https://www.linguee.fr/anglais-francais/traduction/height.html")
