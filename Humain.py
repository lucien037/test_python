from Bipède import Bipede


class Humain(Bipede):
    def __init__(self, energie, food, type_bipede):
        super().__init__(type_bipede)
        self.enrgie = energie
        self.food = food

    def get_energie(self):
        pass

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
