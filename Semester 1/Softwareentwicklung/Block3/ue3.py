import os


class Article:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class StockManager:
    def __init__(self):
        self.run = True
        # add a variable for each shelf space
        self.spaces = {
            "a1": None,
            "a2": None,
            "a3": None,
            "b1": None,
            "b2": None,
            "b3": None
        }
        self.weight = 0
        self.occupied = 0
        self.available = 6
        # add a status which can be printed to the console
        self.status = None

    def add_article(self, place, article):
        print("add article", article.name)
        # check if the current space if available
        # if not, return an error message
        if(self.spaces[place]):
            self.status = "Der ausgewählte Platz ist leider schon belegt!"
        else:
            # if yes, put the article in its place
            self.spaces[place] = article

    def remove_article(self, place):
        # set the space to None again
        if(self.spaces[place]):
            self.spaces[place] = None

    # calculate the current weight and the number items in stock
    def calculate_current_weight_and_stock(self):
        weight = 0
        occupied = 0
        for _, v in self.spaces.items():
            if(v):
                weight = weight + v.weight
                occupied = occupied + 1
        self.weight = weight
        self.occupied = occupied
        self.available = 6 - occupied

    def next_tick(self):
        userInput = input(
            "(a) zum hinzufügen, (r) zum entnehmen und (q) zum beenden drücken: ")
        if(userInput == "a"):
            # check if a new article can be added. If not, return a message
            if(self.available == 0):
                self.status = "Das Regal ist voll. Es kann kein neuer Artikel hinzugefügt werden."
            else:
                # create a new article
                name = input("Wie ist der Name des neuen Artikels? ")
                weight = float(
                    input("Was ist das Gewicht des neuen Artikels? "))
                # ask in which place it should belong
                # if the place is occupied, ask for another place
                place = input("An welchen Platz soll der neue Artikel abgelegt werden? ")
                # add the new article
                article = Article(name, weight)
                self.add_article(place, article)
        if(userInput == "r"):
            # ask from which place the article should be removed
            place = input("Vom welchen Platz soll der Artikel entnommen werden? ")
            self.remove_article(place)
        if(userInput == "q"):
            self.run = False

    def print_current_stock(self):
        for k in self.spaces.keys():
            if(self.spaces[k]):
                print(k, ":", self.spaces[k].name)
            else:
                print(k, ": Leer")

    def print_status(self):
        self.calculate_current_weight_and_stock()
        print("Verfügbare Plätze: ", self.available)
        print("Belegte Plätze: ", self.occupied)
        print("Gesamt Gewicht: ", self.weight)
        if(self.status):
            print("")
            print(self.status)
            print("")
            self.status = None

    def start(self):
        while self.run:
            os.system("clear")
            self.print_current_stock()
            print("")
            self.print_status()
            self.next_tick()


s = StockManager()
s.start()
