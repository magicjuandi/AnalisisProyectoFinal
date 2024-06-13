from MagicFactory import MagicFactory
from Potion import Potion
from Spell import Spell
class HealingMagicFactory(MagicFactory):
    def create_spell(self):
        return Spell("Heal Spell")

    def create_potion(self):
        return Potion("Healing Potion")