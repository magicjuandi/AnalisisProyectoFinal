from Spell import Spell
class SpellDecorator(Spell):
    def __init__(self, spell):
        self.spell = spell

    def cast(self):
        self.spell.cast()