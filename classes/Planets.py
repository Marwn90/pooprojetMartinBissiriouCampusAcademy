
from Parent import Parent
# Création de la classe



"""
class Planets: 
    def __init__(self, name, rotation_period, diameter, climate, gravity, terrain, population, resident, created, edited, url):
        self.name = name
        self.rotation_period = rotation_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.population =  population
        self.resident = resident
        self.created = created
        self.edited = edited
        self.url = url
        """






class Planets(Parent):
      def __init__(self, name, rotation_period, diameter, climate, gravity, terrain, population, resident, created, edited, url):
        self.name = name
        self.rotation_period = rotation_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.population =  population
        self.resident = resident


        # Definition des methodes

def contient(self, message):
    print("{}  a contenir: {}".format(self.name, message))
    return message


# instanciation ou (Creation ) de l'objet vehicles

# Creation du premier objet planet1

planete1 = Planets("Jupyter","1j9h56","48794 km", "chaud", "9,807 m/s2" ,"1000 KM", "0 habitant", "1222","cliptonien", "1800","https://www.porsche.com/france/fuel-consumption/")

# Creation du premier objet planet1

planete2 = Planets("terre", "0j10h42m", "50724 km","humide","10,44 m/s2","1000 KM", "6 milliards", "1222", "terrien", "1000", "https://www.porsche.com/france/fuel-consumption/")
   

        

  
