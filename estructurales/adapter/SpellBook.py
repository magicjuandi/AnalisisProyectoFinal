class SpellBook:
    def __init__(self):
        self.spells = {
            "fireball": "Fireball spell",
            "heal": "Healing spell",
            "lightning": "Lightning spell"
        }

    def get_spell(self, spell_name):
        return self.spells.get(spell_name.lower(), "Unknown spell")