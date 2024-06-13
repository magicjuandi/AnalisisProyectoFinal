class SpellShop:
    def __init__(self):
        self.spells = []

    def add_spell(self, spell):
        self.spells.append(spell)

    def accept(self, visitor):
        for spell in self.spells:
            spell.accept(visitor)