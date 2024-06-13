from SpellShop import SpellShop
class MagicShopFacade:
    def __init__(self):
        self.spell_shop = SpellShop()

    def create_spell(self, spell_name, price):
        self.spell_shop.create_spell(spell_name)
        self.spell_shop.set_spell_price(spell_name, price)

    def show_spell_list(self):
        self.spell_shop.display_spell_list()