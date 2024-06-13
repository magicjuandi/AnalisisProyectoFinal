class Spell:
    def __init__(self, name):
        self.name = name

    def cast(self, wizard):
        print(f"{wizard.name} casts '{self.name}' spell.")