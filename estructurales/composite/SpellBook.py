from MagicComponent import MagicComponent
class SpellBook(MagicComponent):
    def __init__(self):
        self.spells = []

    def add_spell(self, spell):
        self.spells.append(spell)

    def display(self):
        for spell in self.spells:
            spell.display()