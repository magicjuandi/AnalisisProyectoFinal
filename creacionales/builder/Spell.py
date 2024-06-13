class Spell:
    def __init__(self):
        self.name = None
        self.effects = []
        self.level = None

    def __str__(self):
        return f"Spell: {self.name}, Level: {self.level}, Effects: {', '.join(self.effects)}"
