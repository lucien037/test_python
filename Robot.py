from Bipède import Bipede


class Robot(Bipede):
    def __init__(self, energie, instruction, type_bipede):
        super().__init__(type_bipede)
        self.energie = energie
        self.instruction = instruction

    def get_energie(self):
        pass

    def set_energie(self,energie):
        pass