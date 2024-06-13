from Spell import Spell
class SpellFactory:
    @staticmethod
    def create_spell(name):
        return Spell(name)