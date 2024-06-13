from SpellShop import SpellShop
from FireSpell import FireSpell
from HealSpell import HealSpell
from WizardVisitor import WizardVisitor
if __name__ == "__main__":
    shop = SpellShop()
    shop.add_spell(FireSpell())
    shop.add_spell(HealSpell())

    visitor = WizardVisitor()
    shop.accept(visitor)