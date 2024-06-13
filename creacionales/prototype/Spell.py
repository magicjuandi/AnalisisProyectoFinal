import copy

class Spell:
    def __init__(self, name, effects):
        self.name = name
        self.effects = effects

    def __str__(self):
        return f"Spell: {self.name}, Effects: {', '.join(self.effects)}"

    def clone(self):
        return copy.deepcopy(self)