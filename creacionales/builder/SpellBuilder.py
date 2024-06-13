from Spell import Spell
class SpellBuilder:
    def __init__(self):
        self.spell = Spell()

    def set_name(self, name):
        self.spell.name = name
        return self

    def add_effect(self, effect):
        self.spell.effects.append(effect)
        return self

    def set_level(self, level):
        self.spell.level = level
        return self

    def build(self):
        return self.spell