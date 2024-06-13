from SpellDecorator import SpellDecorator
class IceSpell(SpellDecorator):
    def cast(self):
        super().cast()
        print("Ice spell effect added.")
