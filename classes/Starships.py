
# Création de la classe


from Parent import Parent


class Starships:
    def __init__(self, name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, hyperdrive_rating, MGLT, starship_class, pilots, films, created, edited, url):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_athmosphering_speed = max_atmosphering_speed
        self.crew = crew
        self.passengers = passengers
        self.cargo_capacity  = cargo_capacity
        self.consumables = consumables
        self.hyperdrive_rating = hyperdrive_rating
        self.Mglt = Mglt
        self.starship_class = starship_class
        self.pilots = pilots
        self.film = films
        self.created= created
        self.edited = edited
        self.url = url



class Starships(Parent):
     def __init__(self, name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, hyperdrive_rating, MGLT, starship_class, pilots, films, created, edited, url):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_athmosphering_speed = max_atmosphering_speed
        self.crew = crew
        self.passengers = passengers
        self.cargo_capacity  = cargo_capacity
        self.consumables = consumables
        self.hyperdrive_rating = hyperdrive_rating
        self.Mglt = Mglt
        self.starship_class = starship_class
        self.pilots = pilots
        self.film = films

# Definition des methodes


def deplace(self, message):
    print("{}  a deplacé : {}".format(self.name, message))
    return message

        # Création de l'objet Starships

    Starships1 = Starships ("Diamant-B", "Tournesol", "Elon Musk", "200million","18m", "25 tonnes", "317N","20", "130kg", "8000 kerosene" )
      