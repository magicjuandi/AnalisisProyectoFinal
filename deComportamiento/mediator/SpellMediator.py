class SpellMediator:
    def __init__(self):
        self._spell_registry = {}

    def register_spell(self, spell_name, spell):
        self._spell_registry[spell_name] = spell

    def cast_spell(self, spell_name, wizard):
        if spell_name in self._spell_registry:
            self._spell_registry[spell_name].cast(wizard)
        else:
            print(f"Spell '{spell_name}' is not available.")