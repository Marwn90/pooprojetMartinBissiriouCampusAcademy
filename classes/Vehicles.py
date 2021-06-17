

from Parent import Parent

"""
class Vehicles:
    pass

name = Vehicles()
model = Vehicles()
manufacturer = Vehicles()
cost_in_credits = Vehicles
length = Vehicles()
max_atmosphering_speed = Vehicles()
crew = Vehicles()
cargo_capacity = Vehicles()
consumables = Vehicles()
vehicle_class = Vehicles()
pilots = Vehicles()
films = Vehicles()
created = Vehicles()
"""












 
# Création de la classe Véhicles

"""
class Vehicles:
    def __init__(self, name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, vehicle_class, pilots, films, created, edited, url):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
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


class Vehicles(Parent):
    def __init__(self, name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, vehicle_class, pilots, films,):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
        self.crew = crew
        self.passengers = passengers
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.vehicle_class = vehicle_class
        self.pilots = pilots
        self.films = films



# Definition des methodes

def demarre(self, message):
    print("{}  a demarrer : {}".format(self.name, message))
    return message


def transport(self):
    print("transporter des machandises")
    
        
# instanciation ou (Creation ) de l'objet vehicles

# Creation du premier objet vehicles1

vehicles1 = Vehicles ("porsche", "911 GT3", "Volkswagen AG", "200000 euros", "2457 m", "318 km/h", "6 cylindres à plat", "Couple", "510 ch", "97 - 8,9 l/100 km", "sport", "Ferdinand Porsche Ferdinand", "porscheallemand", "1999","23RG", "https://www.porsche.com/france/fuel-consumption/")
print("le nom de mon vehicle est : ", vehicles1.name)
print("le modéle de mon vehicule est : ",vehicles1.model)

# Creation du second objet vehicles2
vehicles2 = Vehicles("Bentley", "911 GT3", "Golf ", "250000 euros", "2,234 m", "217km/h", "6 cylindres à plat / 4 996 cm3", "4 siege", "760 ch", "7,7 - 8,9 l/100 km", "sport", "Harry Guyanne", "BentleyEngland", "1998","83RG", "https://www.bentley.com/france/fuel-consumption/")
print("le nom de mon vehicle2 est : {}".format(vehicles2.name) )
print("le cout de mon vehicle est  : ", vehicles2.cost_in_credits)


# Affichage du cout de l'achat du vehicles1

vehicles1.cost_in_credits = "200000 euros"
print("achat de vehicles1 est : {}".format(vehicles1.cost_in_credits))

#programme principal
vehicles1 = Vehicles("porsche", "911 GT3")

vehicles1.demarre("hoooo hooo ! :")
