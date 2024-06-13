class Wizard:
    def __init__(self, name):
        self.name = name

    def cast_spell(self, spell_name):
        print(f"{self.name} casts {spell_name} spell.")