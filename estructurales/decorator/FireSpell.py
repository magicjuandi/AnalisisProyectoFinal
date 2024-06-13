from SpellDecorator import SpellDecorator
class FireSpell(SpellDecorator):
    def cast(self):
        super().cast()
        print("Fire spell effect added.")