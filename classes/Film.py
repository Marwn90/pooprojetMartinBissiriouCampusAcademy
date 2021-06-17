



from Parent import Parent
# Création de la classe
"""
class Film:
    def __init__(self, name, model, manufacturer, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, vehicle_class,pilots, films, created, edited, url):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.length = length
        self.max_athmosphering_speed = max_atmosphering_speed
        self.crew = crew
        self.passengers = passengers
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.vehicle_class = vehicle_class
        self.pilots = pilots
        self.films = films
        self.created = created
        self.edited = edited
        self.url = url
        """

class Film(Parent):
     def __init__(self, name, model, manufacturer, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, vehicle_class,pilots, films, created, edited, url):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.length = length
        self.max_athmosphering_speed = max_atmosphering_speed
        self.crew = crew
        self.passengers = passengers
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.vehicle_class = vehicle_class
        self.pilots = pilots
        self.films = films


# Definition des methodes

def diffuse(self, message):
    print("{}  a diffuser : {}".format(self.name, message))
    return message

  # Creation de l'objet Film
  # Creation du premier objet film1
    film1 = Film( "Amor", "Romance", "Leornado", "2h", "normale", "herbillon", "Allemand","17Go","petie","comedie","remor", "legendary", "1809", "Samarin", "https://www.linguee.fr/anglais-francais/traduction/height.html")















