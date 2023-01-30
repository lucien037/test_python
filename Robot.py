from Bipède import Bipede


class Robot(Bipede):
    def __init__(self, energie, nom, prix, origine):
        super().__init__(nom, origine, energie)
        self.energie = energie
        self.marque = "OpenIA"
        self.matiere = "Titane"
        self.prix = prix

    def set_energie(self, energie):
        pass

    def execute_instruction(self, instruction):
        pass