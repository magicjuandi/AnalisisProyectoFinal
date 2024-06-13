from RealSpell import RealSpell
class SpellProxy:
    def __init__(self, spell_name):
        self._real_spell = RealSpell(spell_name)

    def cast(self, wizard):
        print("Proxy checks wizard's credentials before casting.")
        if self.check_access(wizard):
            self._real_spell.cast(wizard)

    def check_access(self, wizard):
        # Simulated access control
        return wizard.name == "Gandalf"