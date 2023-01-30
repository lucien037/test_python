class Bipede:

    def __init__(self, nom, origine, energie):
        self.nbJambes = 2
        self.__nom = nom
        self.enrgie = energie
        self.origine = origine

    def get_name(self):
        return self.__nom

    def marcher(self, energie, point_a, point_b):
        pass

    def get_energie(self):
        pass

    def set_energie(self, energie):
        pass
