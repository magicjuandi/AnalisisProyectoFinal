from SpellElement import SpellElement
class HealSpell(SpellElement):
    def accept(self, visitor):
        visitor.visit_heal_spell(self)