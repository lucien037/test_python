from Bipède import Bipede


class Humain(Bipede):
    def __init__(self, energie, food, nom, origine):
        super().__init__(nom, origine, energie)
        self.food = food

    def get_food(self):
        pass

    def donner_ordre(self, ordre):
        pass

    def recharger_robot(self):
        pass

    def reparer_robot(self, robot):
        pass

    def manger(self):
        pass
