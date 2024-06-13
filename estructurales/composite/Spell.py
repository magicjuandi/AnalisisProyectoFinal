from MagicComponent import MagicComponent
class Spell(MagicComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Spell: {self.name}")