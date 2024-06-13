class SpellBook:
    def __init__(self):
        self.spells = ["Fireball", "Heal", "Lightning"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.spells):
            spell = self.spells[self.index]
            self.index += 1
            return spell
        else:
            raise StopIteration