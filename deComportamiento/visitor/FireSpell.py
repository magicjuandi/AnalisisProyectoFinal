from SpellElement import SpellElement
class FireSpell(SpellElement):
    def accept(self, visitor):
        visitor.visit_fire_spell(self)